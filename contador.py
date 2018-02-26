#!/usr/bin/python3
"""
Ejercicio Contador: Programa que funciona como Contador de 5 a 0.
El programa tendra una funcion con una variable global, que cada vez que se le pide un valor nos mostrara el estado del contador y lo reducira. Este contador ira de 5 a 0 y se reiniciara. 
Juan Ureña
j.urenag@alumnos.urjc.es
SAT(URJC)
"""

import sys

status=0

def contador():
    global status
    if status==0:
        status=5
    else:
        status=status-1
        
    print('devuelvo')   
    return status 
    
    





