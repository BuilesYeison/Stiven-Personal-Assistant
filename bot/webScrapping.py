import requests #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4

def weather(): #web scrapping a pagina de clima apra obtener el clima de hoy en medellin
    #no funciona
    url = "https://www.clima.com/colombia/antioquia/medellin"
    page = requests.get(url)
    print(page)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup)

    results = soup.find_all("section", class_="-block-i-1 c-tib")
    for result in results:
        print(result.text)

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

def shopping(keyword):
    #amazon no deja automatizar sin permiso ajajaj
    itemImg = []
    itemTitle = []
    itemPrice = []
    itemLink = []

    keyword = keyword.lower()
    keyword = keyword.replace(" ", "+")
    url = f"https://www.amazon.com/s?k={keyword}&__mk_es_US=ÅMÅŽÕÑ&ref=nb_sb_noss"
    #url = "https://www.clima.com/colombia/antioquia/medellin"
    page = requests.get(url)
    print(page)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup)

    results = soup.find_all("p", class_="a-link-normal a-text-normal")
    for result in results:
        print(result.text)
        
    print(itemLink)


    
