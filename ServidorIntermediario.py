import socket
import numpy as np
import pickle

mi_socket = socket.socket()
mi_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mi_socket.bind( (socket.gethostname(), 8000) )
mi_socket.listen(5)
conexion = socket.socket()
flag = False
tablero = np.array([['0','0','0','0','0','0'], 
                    ['0','0','0','0','0','0'], 
                    ['0','0','0','0','0','0'],
                    ['0','0','0','0','0','0'],
                    ['0','0','0','0','0','0'],
                    ['0','0','0','0','0','0']])

win = False
draw = False


import numpy as np

'''
Funcion ganar
Retorna True si encuentra 4 seguidos o False si no,
Busca usando 4 metodos distintos que el simbolo de jugador se repita 4 veces seguidas en un cierto patron
'''

def ganar(matriz, jugador):
    # Horizontal
    for fila in range(matriz.shape[0]):
        for columna in range(matriz.shape[1] - 3):
            if all(matriz[fila, columna + i] == jugador for i in range(4)):
                return True

    # Vertical
    for columna in range(matriz.shape[1]):
        for fila in range(matriz.shape[0] - 3):
            if all(matriz[fila + i, columna] == jugador for i in range(4)):
                return True

    # Diagonal a la izquierda
    for fila in range(matriz.shape[0] - 3):
        for columna in range(matriz.shape[1] - 3):
            if all(matriz[fila + i, columna + i] == jugador for i in range(4)):
                return True

    # Diagonal a la derecha
    for fila in range(matriz.shape[0] - 3):
        for columna in range(3, matriz.shape[1]):
            if all(matriz[fila + i, columna - i] == jugador for i in range(4)):
                return True

    return False

'''
Funcion empate
Retorna true si toda la matriz esta ocupada, y falso si hay algun 0

Revisa matriz por si existe algun 0 en un espacio
'''

def empate(matriz):
    return np.all(matriz != "0")




while True:

    if flag == False: #Se ejecuta una sola vez para aceptar conexion con cliente y con servidor go
        conexion, addr = mi_socket.accept()
        print("Nueva conexion establecida")
        print(addr)
        peticionbyte = conexion.recv(1024) #mensaje recibido del cliente
        peticion = peticionbyte.decode('utf-8')
        mi_socket2.sendto(peticion.encode('utf-8'), ('127.0.0.1', 1234))
        print("Mensaje enviado al Servidor Conecta 4: ",peticion)

        if peticion == '2':
            mensaje = "cerrar"
            mi_socket2.sendto(mensaje.encode('utf-8'), ('127.0.0.1', 1234))
            conexion.close()
            mi_socket.close()
            mi_socket2.close()
            break
            #cerrar todo
        else:
            print("Mensaje recibido del cliente: ", peticion)
            data, address = mi_socket2.recvfrom(1024)
            print(f"Mensaje recibido de conecta4 {address}: {data.decode('utf-8')}")
            flag = True

    #Reemplaza valor del cliente en tablero
    fila = 5
    peticion2 = conexion.recv(1024)
    jugada = peticion2.decode('utf-8')
    

    #A partir de la jugada recibida, lo ingresa al tablero

    if jugada == '1':
        
        while tablero[fila][0] != '0' and fila >= 0:
            fila -= 1
        if fila >= 0:
            tablero[fila][0] = 'A'
            
    elif jugada == '2':
        while tablero[fila][1] != '0' and fila >= 0:
            fila -= 1
        if fila >= 0:
            tablero[fila][1] = 'A'
        
    elif jugada == '3':
        while tablero[fila][2] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            tablero[fila][2] = 'A'
        
    elif jugada == '4':
        while tablero[fila][3] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            tablero[fila][3] = 'A'
        
    elif jugada == '5':
        while tablero[fila][4] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            tablero[fila][4] = 'A'

    elif jugada == '6':
        while tablero[fila][5] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            tablero[fila][5] = 'A'
    
    #Si las funciones retorna true se activan flags
    if empate(tablero):
        print("Hay un empate")
        mensaje = '5'
        draw = True

    if ganar(tablero, 'A'):
        print("Gana cliente")
        mensaje = '3'
        win = True

    

    #Puerto dinamico

    puerto = mi_socket2.recv(1024).decode('utf-8')  #Recibo puerto del go
    print(f"Mensaje recibido de conecta4 {address}: {data.decode('utf-8')}")
    print("Puerto a usar: "+puerto)

    if jugada == "cerrar": #En caso de no querer continuar el juego
        socketDinamico = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creo un socket dinamico que manda un mensaje y se cierra
        socketDinamico.connect(('127.0.0.1', int(puerto)))
        socketDinamico.send(jugada.encode('utf-8'))
        print("Mensaje enviado al servidor conecta 4: ",jugada)

        socketDinamico.close()
        conexion.close()
        mi_socket2.close()
        mi_socket.close()
        break

        
    #Abrimos socket con puerto dinamico

    socketDinamico = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Se crea socket dinamico que manda un mensaje al servidor go y se cierra
    socketDinamico.connect(('127.0.0.1', int(puerto)))

    socketDinamico.send(jugada.encode('utf-8'))
    print("Mensaje enviado al servidor conecta 4: ",jugada)

    
    
        
    jugadago = socketDinamico.recv(1024).decode('utf-8') #Se almacena jugada del go
    print(f"Jugada recibido de conecta4: "+jugadago)  #Recibe jugada del go    

    socketDinamico.close()


    ##Incorpora ficha del bot a el tablero
    fila = 5
    if win == False and draw == False:
        if jugadago== '0':
            
            while tablero[fila][0] != '0' and fila >= 0:
                fila -= 1
            if fila >= 0:
                tablero[fila][0] = 'M'
                
        elif jugadago == '1':
            while tablero[fila][1] != '0' and fila >= 0:
                fila -= 1
            if fila >= 0:
                tablero[fila][1] = 'M'
            
        elif jugadago == '2':
            while tablero[fila][2] != '0' and fila >= 0:
                fila -= 1
                
            if fila >= 0:
                tablero[fila][2] = 'M'
            
        elif jugadago == '3':
            while tablero[fila][3] != '0' and fila >= 0:
                fila -= 1
                
            if fila >= 0:
                tablero[fila][3] = 'M'
            
        elif jugadago == '4':
            while tablero[fila][4] != '0' and fila >= 0:
                fila -= 1
                
            if fila >= 0:
                tablero[fila][4] = 'M'

        elif jugadago == '5':
            while tablero[fila][5] != '0' and fila >= 0:
                fila -= 1
                
            if fila >= 0:
                tablero[fila][5] = 'M'


    print(tablero)

    tablero_bytes = pickle.dumps(tablero) #Comprime tablero en bytes
    conexion.send(tablero_bytes)  #Mandamos tablero actualizado al cliente
    print("Tablero enviado al cliente")
    

    #Checkeamos ganador
    if win == True:  #Si flag esta activa, se manda senal 3 a cliente y se terminan procesos
        mensaje = '3'
        jugada = "cerrar"
        puerto = mi_socket2.recv(1024).decode('utf-8')  #Recibo puerto del go
        print("Puerto a usar para enviar mensaje es:"+puerto)
        socketDinamico = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketDinamico.connect(('127.0.0.1', int(puerto)))
        socketDinamico.send(jugada.encode('utf-8'))
        print("Mensaje enviado al servidor conecta 4: ",jugada)
        conexion.send(mensaje.encode('utf-8'))

        socketDinamico.close()
        conexion.close()
        mi_socket2.close()
        mi_socket.close()
        break


    if draw == True: #Senal activa de empate
        mensaje = '5'
        jugada = "cerrar"
        puerto = mi_socket2.recv(1024).decode('utf-8')  #Recibo puerto del go
        print("Puerto a usar para enviar mensaje es:"+puerto)
        socketDinamico = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketDinamico.connect(('127.0.0.1', int(puerto)))
        socketDinamico.send(jugada.encode('utf-8'))
        print("Mensaje enviado al servidor conecta 4: ",jugada)
        conexion.send(mensaje.encode('utf-8'))

        socketDinamico.close()
        conexion.close()
        mi_socket2.close()
        mi_socket.close()
        break


    if ganar(tablero, 'M'):  #Ganador es el bot
        print("Gana bot")
        mensaje = '4'
        conexion.send(mensaje.encode('utf-8'))
        jugada = "cerrar"
        puerto = mi_socket2.recv(1024).decode('utf-8')  #Recibo puerto del go
        print("Puerto a usar para enviar mensaje es:"+puerto)
        socketDinamico = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketDinamico.connect(('127.0.0.1', int(puerto)))
        socketDinamico.send(jugada.encode('utf-8'))
        print("Mensaje enviado al servidor conecta 4: ",jugada)

        socketDinamico.close()
        conexion.close()
        mi_socket2.close()
        mi_socket.close()

        break

    else:  #Se manda un mensaje que no activa nada en el lado del cliente para suplir receive tcp
        mensaje = '6'
        conexion.send(mensaje.encode('utf-8'))



    

    
