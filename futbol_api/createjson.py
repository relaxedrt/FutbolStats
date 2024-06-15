import json
import getstats
from datetime import datetime

def getRanking():

    #Definimos la lista
    ranking = {}

    with open("ranking.json", "w") as file:

        #Entramos en un bucle de todos los archivos
        for i in range(1,503):
            print(i)
            #Asignamos a la url el valor de i
            url = f"https://www.bdfutbol.com/es/e/e{i}.html?p=stats"
            
            soup = getstats.getContent(url)
            
            if getstats.getError(soup) != "Error 404":

                #Definimos el diccionario
                team = {
                    "name":f"{getstats.getName(soup)}",
                    "matches":f"{getstats.calcMatches(soup)}",
                    "wins":f"{getstats.calcWins(soup)}",
                    "loss":f"{getstats.calcLoss(soup)}"
                }
                
                #Añadimos el equipo a la lista
                ranking[i]=team
        fecha = {f"{datetime.now()}":ranking}
        json.dump(fecha, file, indent=4)
    return
        

if __name__ == "__main__":
    init = datetime.now()
    getRanking()
    end = datetime.now()
    total = end - init
    print(total)