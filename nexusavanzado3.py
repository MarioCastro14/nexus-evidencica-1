import sys
import pandas as pd
import numpy as np
import sqlite3
from sqlite3 import Error

Alumnos = {"Hugo" : {}, "Sergio" : {}, "Mario" : {}, "Kevin" : {}, "Alberto" :{}, \
           "Felipe" : {}, "Cristian" : {}, "Luis" : {}, "Angel" : {}, "Adamaris" : {}, \
           "Mariana" : {}, "Elena" : {}, "Cristal" : {}, "Cristina" : {}, "Karla" : {}, \
           "Lizbeth" : {}, "Fernanda" :{}, "Aracely" : {}, "Ilena" : {}, "Norma" : {}, \
           "Janeth": {}, "Erick" :{}, "Daniel" : {}, "Juan" : {}, "Ivan" : {}, \
           "Brenda": {}, "Rubi" : {}, "Kate" : {}, "Alma" : {}, "Gignac" : {}}
  
  
diccionario_materia= {"Programacion" : {}, "Base De Datos": {}, "Creatividad": {}, "Contabilidad" :{}, "Economia" :{}}


x=Alumnos.keys()
Alumnoskeys = pd.DataFrame(x)
framematerias = pd.DataFrame(diccionario_materia)
framealumnos = pd.DataFrame(Alumnoskeys)
concatenacion = pd.concat([framealumnos, framematerias], axis=0)

diccionarioc1 = []
diccionarioc2 = []
diccionarioc3 = []
diccionarioc4 = []
diccionarioc5 = []

Numero1=0
Numero2=0
Numero3=0

Proceso=True
while Proceso == True:
    print("1 para ver a los usuarios y sus calificaciones")
    print("2 para subir calificaciones")
    print("3 para ver la estadistica descriptiva de las materias")
    print("4 para ver a los alumnos reprobados")
    print("5 para salir")

    Proceso2= int(input("¿Que quieres realizar?:"))
   
    if Proceso2 == 1:
        print(concatenacion.iloc[:,0])
    
    
    elif Proceso2 == 2:
        for i in range(1):
            try:
                Nombres=Alumnoskeys.iloc[Numero2, 0]
                print(f"Calificación para el alumno {Numero3} en la lista")
                c1= int(input("Dime la calificacion en Base De Datos: "))
                c2= int(input("Dime la calificacion en Contabilidad: "))
                c3= int(input("Dime la calificacion en Creatividad: "))
                c4= int(input("Dime la calificacion en Economia: "))
                c5= int(input("Dime la calificacion en Programacion: "))
                concatenacion.loc[Numero1] = [Nombres, c1, c2, c3, c4, c5]
                if c1 < 70:
                    diccionarioc1.append((Nombres, c1))
                if c2 < 70:
                    diccionarioc2.append((Nombres, c2))
                if c3 < 70:
                    diccionarioc3.append((Nombres, c3))
                if c4 < 70:
                    diccionarioc4.append((Nombres, c4))
                if c5 < 70:
                    diccionarioc5.append((Nombres, c5))
                Numero1 = Numero1+1
                Numero2 = Numero2+1
                Numero3 = Numero3+1
                print(concatenacion)
            except Error as e:
                print(e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")



    elif Proceso2 == 3:
        print(concatenacion.describe())
    
    
    elif Proceso2 == 4:
            print(f"Calificaciones reprobatorias de Base de Datos {diccionarioc1}")
            print(f"Calificaciones reprobatorias de Contabilidad {diccionarioc2}")
            print(f"Calificaciones reprobatorias de Creatividad {diccionarioc3}")
            print(f"Calificaciones reprobatorias de Economia {diccionarioc4}")
            print(f"Calificaciones reprobatorias de Programacion{diccionarioc5}")
                
    
    
    elif Proceso2 == 5:
        print("Fin del programa")
        Proceso= False