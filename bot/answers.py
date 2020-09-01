import random
from datetime import datetime

#diferentes respuestas a diferentes solicitudes del usuario

def greetAnswers():
    now = datetime.now()
    now = int(now.hour)     
    responses = []
    if now in range(4, 12):
        responses = ["Hola buenos dias Yeison!!","Hola, buena mañana Yeison!!", "Buen día Yeison, que te rinda el día!!", "Buenos dias, recuerda desayunar y hacer ejercicio!!"]  
    elif now in range(12, 19):
        responses = ["Hola, buenas tardes Yeison!!", "Buena tarde Yeison, en que te puedo ayudar?", "Hola, disfruto de la tarde Yeison!! en que te puedo ayudar?", "Buenas tardes Yeison!! Recuerda comer saludable", "Buenas tardes Yeison, recuerda tus tareas jajaja, en que te puedo ayudar?"]
    elif now in range(19, 25) or now in range(1, 4):
        responses = ["Hola, buenas noches Yeison!!", "Hola Yeison!! Que disfrutes la noche, en que te puedo ayudar?", "Hola Yeison!! Recuerda no dormirte tan tarde!!", "Buenas noches caballero, en que te puedo ayudar??"]
    else:
        responses=["oopss", "wtf"]


    answer = random.choice(responses)
    return answer

def thanksAnswers():
    answers = ["¡¡De nada Yeison, para servirte!!😎", "¡¡Espero que sea de ayuda💪!!", "¡¡Pasostamos!!🤙", "¡¡Es un placer servirte!!😺"]
    answer = random.choice(answers)
    return answer

def pleaseAnswers():
    answers = ["Claro que si!!", "Dame un momento", "Estoy trabajando en ello"]
    answer = random.choice(answers)
    return answer
