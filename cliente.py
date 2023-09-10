import socket
import numpy as np

mi_socket = socket.socket()
mi_socket.connect( (socket.gethostname(), 8000) )

print("- - - - - - - - Bienvenido al Juego - - - - - - - -")
Seleccion =input("- Seleccione una opción\n1-Jugar\n2-Salir\n")
if Seleccion == '1':
    Seleccion_bytes = Seleccion.encode('utf-8')
    mi_socket.send(Seleccion_bytes)
    
    respuesta = mi_socket.recv(1024)
    print("Respuesta de disponibilidad: ", respuesta,"\n")
    print("- - - - - - - - Comienza el Juego - - - - - - - -")
    
    tablero = np.array([[0,0,0,0,0,0], 
               [0,0,0,0,0,0], 
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0]])
    print("Tablero inicial:\n",tablero)
    
    
else:
    
    Seleccion_bytes = Seleccion.encode('utf-8')
    mi_socket.send(Seleccion_bytes)
    
    respuesta = str(mi_socket.recv(1024))
    print("Respuesta de disponibilidad: ", respuesta)    

'''
mensaje = "Hola, te saludo desde el cliente!"
mensaje_bytes = mensaje.encode('utf-8')

mi_socket.send(mensaje_bytes)
respuesta = mi_socket.recv(1024)

print(respuesta)
mi_socket.close()
    
'''
