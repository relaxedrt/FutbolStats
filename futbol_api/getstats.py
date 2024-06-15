import requests
from datetime import datetime
from bs4 import BeautifulSoup

#Definimos la url donde se encuentran las estadisticas del racing
# url = "https://www.bdfutbol.com/es/e/e29.html?p=stats"
#Solo hay hasta el equipo e503

def calcWins(soup):

    #Buscamos el div que guarda las estadisticas
    stats = soup.find("div", class_="stats")

    #Filtramos los div con esa clase de mierda en una lista
    windiv = stats.find_all("div", class_="col-md-12 f12 pt-2 pb-2 font-blue")

    #Lo volvemos a filtrar con otra clase
    windiv2 = windiv[1].find_all("div", class_="font-weight-bold")

    #Sacamos la primera de la lista que son las victorias
    wins = windiv2[0].get_text()

    #Buscamos donde está el # porque son unos cabrones y han evitado que lo hagamos a toda costa
    indice = wins.find('#')

    #Lo convertimos a entero
    wins = int(wins[:indice])

    #Devolvemos las victorias
    return wins

def calcMatches(soup):

    #Buscamos el div que guarda las estadisticas
    stats = soup.find("div", class_="stats")

    #Filtramos los div con esa clase de mierda en una lista
    windiv = stats.find_all("div", class_="col-md-12 f12 pt-2 pb-2 font-blue")

    #Lo volvemos a filtrar con otra clase
    windiv2 = windiv[0].find_all("div", class_="font-weight-bold")

    #Sacamos la primera de la lista que son las victorias
    matches = windiv2[0].get_text()

    #Buscamos donde está el # porque son unos cabrones y han evitado que lo hagamos a toda costa
    indice = matches.find('#')

    #Lo convertimos a entero
    matches = int(matches[:indice])

    #Devolvemos las victorias
    return matches


def calcLoss(soup):

    #Buscamos el div que guarda las estadisticas
    stats = soup.find("div", class_="stats")

    #Filtramos los div con esa clase de mierda en una lista
    windiv = stats.find_all("div", class_="col-md-12 f12 pt-2 pb-2 font-blue")

    #Lo volvemos a filtrar con otra clase
    windiv2 = windiv[2].find_all("div", class_="font-weight-bold")

    #Sacamos la primera de la lista que son las victorias
    loss = windiv2[0].get_text()

    #Buscamos donde está el # porque son unos cabrones y han evitado que lo hagamos a toda costa
    indice = loss.find('#')

    #Lo convertimos a entero
    loss = int(loss[:indice])

    #Devolvemos las victorias
    return loss

def getName(soup):

    #Buscamos el h1 que guarda el nombre
    h1 = soup.find("h1", class_="heroh1 mt-2 mb-2 mb-md-4")
    
    #Encontramos el nombre en el h1
    name = h1.get_text().strip()

    return name

def getError(soup):

    try:
        #Buscamos el h1 que guarda el nombre
        h1 = soup.find("h1", class_="mt-5 mb-3")

        return h1.get_text().strip()
    
    except:
        return None
    
def getContent(url):
    #Hacemos una petición get y parseamos el resultado
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    return soup

if __name__ == "__main__":
    soup = getContent("https://www.bdfutbol.com/es/e/e29.html")
    # print(f"El {getName("https://www.bdfutbol.com/es/e/e29.html?p=stats")} ha jugado {calcMatches("https://www.bdfutbol.com/es/e/e29.html?p=stats")} veces.")
    # print(f"El {getName("https://www.bdfutbol.com/es/e/e29.html?p=stats")} ha ganado {calcWins("https://www.bdfutbol.com/es/e/e29.html?p=stats")} veces.")
    # print(f"El {getName("https://www.bdfutbol.com/es/e/e29.html?p=stats")} ha perdido {calcLoss("https://www.bdfutbol.com/es/e/e29.html?p=stats")} veces.")
    print(getError("https://www.bdfutbol.com/es/e/e29.html?p=stats"))