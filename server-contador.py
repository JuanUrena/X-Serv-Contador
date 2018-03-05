#!/usr/bin/python3
"""
Ejercicio Server Contador: Programa que funciona como Server Contador de 5 a 0.
El programa funcionara como server y cada vez que reciba una solicitud mostrara por pantalla un contador de 5 a 0.
Juan Ureña
j.urenag@alumnos.urjc.es
SAT(URJC)
"""

import sys
import contador
import socket
import random 

#Creamos TCP socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Comprobamos si está en uso el puerto
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Atamos al puerto
name=socket.gethostname()
mySocket.bind((name, 1234))

#Fijamos número máximo de usuarios a 5
mySocket.listen(5)

#Estamos listos para recibir solicitudes

#Parte Principal


while True:
#Recibo mensaje
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('Request received:')
    request=str(recvSocket.recv(2048), 'utf-8')
    resource=request.split()[1]
    print(resource)
   
    if resource=='/contador':      
        URL = "/contador/"+str(random.randrange(999999999))
        answer=("HTTP/1.1 200 OK\r\n\r\n"+"<html><body><h1>Contador Online</h1> <a href="+URL+"> Este es tu contador</a> </body></html>" + "\r\n")
    else:
        answer=("HTTP/1.1 404 NOT FOUND\r\n\r\n" +"<html><body><h1>Contador Online</h1>" +'Recurso no encontrado' + "</body></html>" +"\r\n")
    recvSocket.send(bytes(answer, 'utf-8'))
                       
    recvSocket.close()
    
    
