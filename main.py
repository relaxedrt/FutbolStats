import datetime
import time

file_path = "DayFile.txt" # Establecemos El Nombre Del Archivo Donde Se Guarda El Dia De Ayer
TimeDeath = 60 * 30 # Establecemos El Tiempo Que Va A Tardar Eb Volver A Ejecutarse

def get_Yesterday():
    # Abrimos El txt En Modo Lectura
    with open(file_path, "r") as dayFile:
        # Quitamos Los Corchetes Extraidas Del txt, Lo Lee Como Una Cadena Aunque Tenga Forma De String
        ayer = dayFile.read().strip('[]')
        # Quitamos Las Comas Extraida Del txt Usando El Map Que Va Caracter a Caracter
        ayer = list(map(int, ayer.split(",")))
    return ayer
    
def set_Yesterday():
    with open(file_path, "w") as dayFile:
            dayFile.write(f"{[datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day]}")


if __name__ == '__main__':
    ayer = get_Yesterday()    
    while True:
        # Actualizamos El Dia En Una Array
        hoy = [datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day]
        # Con Comprobar El Dia Bastaria, Pero Asi Estamos Mas Seguros
        if hoy[0] != ayer[0] or hoy[1] != ayer[1] or hoy[2] != ayer[2]:
            # print("hoy " + str(hoy) + " ayer " + str(ayer)) # Comprobacion De Que Se Actualiza
            #Cambiamos El Dia De Ayer En El txt
            set_Yesterday()
            # Cambiamos El Dia De Ayer En La Variable
            ayer = [datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day]

        # print("here " + str(ayer)) # Comprobacion De Que Se Actualiza
        # Esperamos x Tiempo Y Volvemos A Comprobar 
        time.sleep(10)    