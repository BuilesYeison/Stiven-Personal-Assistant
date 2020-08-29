import os
import logging
import telegram
import time
from datetime import datetime
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from answers import greetAnswers, thanksAnswers, pleaseAnswers
from webScrapping import weather, findJobs
import instaloader

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s," 
)
logger = logging.getLogger()

L = instaloader.Instaloader(download_comments=False, max_connection_attempts=9, post_metadata_txt_pattern=None, save_metadata=False, download_video_thumbnails=False, download_geotags=False, filename_pattern="{shortcode}")#init instaloader

"""Agregar:
-Buscar empleos en computrabajo y devolver link (LISTO)
-Crear base de datos con una tabla que tenga el horario de este semestre
-Crear tabla en la base de datos donde pueda agregar recordatorios con fecha, la descripcion de la actividad, tipo de actividad
-Dar ultimas noticias de videojuegos(LISTO)
-Dar ultimas noticias de colombia y/o el mundo (instaloader)(LISTO)
-solicitar contraseña para informacion delicada
-No funciona el clima"""


TOKEN = os.getenv("TOKEN")

def ping(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    logger.info(f"El bot funciona!!")
    bot.sendMessage(chat_id=chatId, text="pong")

def getPosts(theme):# get posts using instaloader from keyword 'theme'
    date = datetime.now() 
    now = datetime(date.year,date.month,date.day) #get actual time
    isVideo = []
    postUsernames = []
    postShortcodes = []
    postCaptions = []

    if 'juego' in theme:
        PROFILES = ["checkandplay", "instantgaminges", "levelupcom", "3djuegos"]
    elif 'pais' in theme:
        PROFILES =["eltiempo", "revistasemana", "elespectador", "elcolombiano"]

    try:
        for PROFILE in PROFILES:
            logger.info(f'Profile = {PROFILE}')
            time.sleep(2)
            profile = instaloader.Profile.from_username(L.context, PROFILE) #connect with profile
            logger.info('Profile loaded')
            count = 0
            for post in profile.get_posts():
                count += 1
                if post.date >= now: #publish time is today
                    time.sleep(2)
                    download = L.download_post(post, PROFILE)#download post
                    logger.info('Download complete')
                    if download is True:
                        video = post.is_video #verify if is a video
                        postUsernames.append(post.owner_username) #get post values
                        postShortcodes.append(post.shortcode)
                        postCaptions.append(post.caption)
                        if video is True:
                            isVideo.append(True)                                                        
                        else:
                            isVideo.append(False)                          
                                                                                        
                if count == 1:
                    break
            logger.info('Next profile')
    except:
        pass

    return isVideo, postUsernames, postShortcodes, postCaptions #send listo with of all of posts info found


def echo(update, context): #obtener el mensaje que envio el usuario e identificar palabra clave para responderle con lo que solicita   
    bot = context.bot
    chatId = update.message.chat_id
    updateText = getattr(update, "message", None)
    msgId = updateText.message_id
    text = update.message.text
    text = text.lower() #convertir todo el texto en minuscula

    if "hola" in text:
        answer = greetAnswers()
        bot.sendMessage(chat_id=chatId, text=answer)
    
    if 'favor' in text:
        answer = pleaseAnswers()
        bot.sendMessage(chat_id=chatId, text=answer)

    if "clima" in text:
        try:
            todayWeather = weather()
            bot.sendMessage(chat_id=chatId, parse_mode="HTML", text=f"<b>Este es el clima de hoy Yeison:</b>\n\n{todayWeather}")
        except:
            bot.sendMessage(chat_id=chatId, text="Lo siento por ahora esta funcionalidad no está disponible 😔")

    if "gracias" in text:
        answer = thanksAnswers()
        bot.sendMessage(chat_id=chatId, text=answer)

    if "trabajo" in text:        
        try:
            text = text.split("'") #split the sentence and get the desired work for look
            text = text[1] #get desired work into ' '
            listJobsTittles, hyperlinks, companies, publishTimes, workSites = findJobs(text) #get lists with jobs info about the desired work
            bot.sendMessage(chat_id=chatId, parse_mode= "HTML", text="<b>Aqui estan algunas de las ofertas que pude encontrar:</b>")
            for index in range(len(listJobsTittles)): #get index from all of jobs found
                time.sleep(2)#wait 2 seconds for each job info
                bot.sendMessage(chat_id=chatId,parse_mode="HTML", text=f"<b>Empleo:</b> {listJobsTittles[index]}\n<b>Empresa:</b> {companies[index]}\n<b>Lugar:</b> {workSites[index]}\n<b>Fecha de publicación:</b> {publishTimes[index]}\n\n<b>Link:</b> {hyperlinks[index]}")  
        except:
            bot.sendMessage(chat_id=chatId, text="Lo siento por ahora esta funcion no funciona :C")

    if "noticia" and 'juego' in text:
        answer = pleaseAnswers()
        bot.sendMessage(chat_id=chatId, text=answer)#send message before of collect posts
        try:
            isVideo, postUsernames, postShortcodes, postCaptions = getPosts('juego') #get lists with posts info about 'juegos'
            for index in range(len(isVideo)): #loop each posts index
                if isVideo[index] is True:
                    try:
                        with open(postUsernames[index]+'/'+postShortcodes[index]+'.mp4', 'rb') as f:#get the downloaded post in the getPosts() method
                            bot.send_video(chat_id=chatId, video=f)
                            if postCaption[index] == None: #if the post has not description
                                bot.sendMessage(chat_id=chatId, parse_mode='HTML', text=f'<b>{postUsernames[index]}:</b> None')
                            else: #send message with post description
                                bot.sendMessage(chat_id=chatId, parse_mode='HTML', text=f'<b>{postUsernames[index]}:</b> {postCaptions[index]}')
                    except:
                        pass
                else: #is an image
                    try:
                        with open(postUsernames[index]+'/'+postShortcodes[index]+'.jpg', 'rb') as f:
                            bot.send_photo(chat_id=chatId, photo=f)
                            if postCaptions[index] == None: #if the post has no description
                                bot.sendMessage(chat_id=chatId, parse_mode='HTML', text=f'<b>{postUsernames[index]}:</b> None')
                            else: #send message with post description
                                bot.sendMessage(chat_id=chatId, parse_mode='HTML', text=f'<b>{postUsernames[index]}:</b> {postCaptions[index]}')
                    except:
                        pass
            
                time.sleep(2)
        except:
            bot.sendMessage(chat_id=chatId, text="No esta disponible esta funcion")
        
    if "noticia" and "pais" in text: #get news about Colombia
        #meter todo en try
        answer = pleaseAnswers()
        bot.sendMessage(chat_id=chatId, text=answer)#send message before of collect posts
        isVideo, postUsernames, postShortcodes, postCaptions = getPosts('pais')
        for index in range(len(isVideo)):
            if isVideo[index] is True:
                try:
                    with open(postUsernames[index]+'/'+postShortcodes[index]+'.mp4', 'rb') as f:
                        bot.send_video(chat_id=chatId, video=f)
                        if postCaption[index] == None: #if the post has no description
                            bot.sendMessage(chat_id=chatId, parse_mode='HTML', text=f'<b>{postUsernames[index]}:</b> None')
                        else: #send message with post description
                            bot.sendMessage(chat_id=chatId, parse_mode='HTML', text=f'<b>{postUsernames[index]}:</b> {postCaptions[index]}')
                except:
                    pass
            else:
                try:
                    with open(postUsernames[index]+'/'+postShortcodes[index]+'.jpg', 'rb') as f:
                        bot.send_photo(chat_id=chatId, photo=f)
                        if postCaptions[index] == None: #if the post has no description
                            bot.sendMessage(chat_id=chatId, parse_mode='HTML', text=f'<b>{postUsernames[index]}:</b> None')
                        else: #send message with post description
                            bot.sendMessage(chat_id=chatId, parse_mode='HTML', text=f'<b>{postUsernames[index]}:</b> {postCaptions[index]}')
                except:
                    pass
            
            time.sleep(2)
    
if __name__ == "__main__":
    mybot = telegram.Bot(token=TOKEN)
    updater = Updater(mybot.token, use_context=True)
    dp = updater.dispatcher

dp.add_handler(CommandHandler("ping", ping))
dp .add_handler(MessageHandler(Filters.text, echo)) #get text from chat

updater.start_polling()
print("BOT IS RUNNING")
updater.idle()