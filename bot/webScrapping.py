import requests
from bs4 import BeautifulSoup

def weather(): #web scrapping a pagina de clima apra obtener el clima de hoy en medellin
    #global todayWeather

    #ARREGLAR
    url = "https://weather.com/es-CO/tiempo/hoy/l/c1cdc854c06b7fe145827400f82eb319c2bb41e956f8ac0b52ab94180aed77c4"
    page = requests.get(url)

    #init default var
    prob = 'There is not info yet'
    tittle = 'There is not info yet'
    timestamp = 'There is not info yet'
    actualTemp = 'There is not info yet'
    weather = 'There is not info yet'
    maxmin = 'There is not info yet'
    airQuality = 'There is not info yet'

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('h1', string=lambda text:'tiempo' in text.lower()) #get tittle of time
    for result in results:
        tittle = result.text    
    
    results = soup.find('div', class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--timestamp--1ybTk")
    timestamp = results.text
    timestamp = timestamp.replace('as of','')    

    results = soup.find('span', class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
    actualTemp = results.text

    results = soup.find('div', class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--phraseValue--mZC_p")
    weather = results.text

    results=soup.find_all('div', class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
    for result in results:
        prob = result.text

    results = soup.find_all("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempHiLoValue--3T1DG")
    for result in results:
        maxmin = ""
        maxmin = maxmin + result.text
    maxmin =maxmin.replace('/', '|')

    results = soup.find("span", class_="_-_-components-src-molecule-AirQualityText-AirQualityText--severity--1smy9")
    airQuality = results.text

    todayWeather = f'{tittle}:\n\nTiempo: {timestamp}\nTemperatura Actual: {actualTemp}\nClima: {weather}\nProbabilidad: {prob}\nMax/Min: {maxmin}\nCalidad del aire: {airQuality}\n\nInformacion sacada de la pagina: weather.com'

    return todayWeather

def findJobs(keyword): #web scrapping a pagina de trabajo con palabra clave que envio el usuario para enviarle los trabajos recientes
    listJobsTittles = []
    hyperlinks = []
    companies = []
    publishTimes = []
    workSites = []

    keyword = keyword.lower()
    keyword = keyword.replace(" ", "-")
    url = f"https://www.computrabajo.com.co/trabajo-de-{keyword}-en-antioquia?q={keyword}"
    page = requests.get(url) #get all page info
    soup = BeautifulSoup(page.content,"html.parser")#get page content in html

    results = soup.find_all("a", class_="js-o-link")
    for result in results:
        hyperlink = f"https://www.computrabajo.com.co{result['href']}"
        hyperlinks.append(hyperlink)
        listJobsTittles.append(result.text) 

    results = soup.find_all("a", class_="fc_blue")
    for result in results:
        companies.append(result.text)

    results = soup.find_all("span", class_="dO")
    for result in results:
        publishTimes.append(result.text)
    
    results = soup.find_all(itemprop="addressRegion")
    for result in results:
        workSites.append(result.text)

    return listJobsTittles, hyperlinks, companies, publishTimes, workSites
    
