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


import numpy as np

def check_win(board, player):
    # Check for horizontal wins
    for row in range(board.shape[0]):
        for col in range(board.shape[1] - 3):
            if all(board[row, col + i] == player for i in range(4)):
                return True

    # Check for vertical wins
    for col in range(board.shape[1]):
        for row in range(board.shape[0] - 3):
            if all(board[row + i, col] == player for i in range(4)):
                return True

    # Check for diagonal wins (from top-left to bottom-right)
    for row in range(board.shape[0] - 3):
        for col in range(board.shape[1] - 3):
            if all(board[row + i, col + i] == player for i in range(4)):
                return True

    # Check for diagonal wins (from top-right to bottom-left)
    for row in range(board.shape[0] - 3):
        for col in range(3, board.shape[1]):
            if all(board[row + i, col - i] == player for i in range(4)):
                return True

    return False


while True:
    if flag == False:
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
    


    if check_win(tablero, 'A'):
        print("Gana cliente")
        mensaje = '3'
        win = True

    

    #Puerto dinamico
    puerto = mi_socket2.recv(1024).decode('utf-8')  #Recibo puerto del go
    print(f"Mensaje recibido de conecta4 {address}: {data.decode('utf-8')}")
    print("Puerto a usar: "+puerto)

    if jugada == "cerrar": #En caso de no querer continuar el juego
        socketDinamico = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketDinamico.connect(('127.0.0.1', int(puerto)))
        socketDinamico.send(jugada.encode('utf-8'))
        print("Mensaje enviado al servidor conecta 4: ",jugada)

        socketDinamico.close()
        conexion.close()
        mi_socket2.close()
        mi_socket.close()
        break

        
    #Abrimos socket con puerto dinamico

    socketDinamico = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketDinamico.connect(('127.0.0.1', int(puerto)))


    socketDinamico.send(jugada.encode('utf-8'))
    print("Mensaje enviado al servidor conecta 4: ",jugada)

    
    
        
    jugadago = socketDinamico.recv(1024).decode('utf-8')
    print(f"Jugada recibido de conecta4: "+jugadago)  #Recibe jugada del go    

    socketDinamico.close()


    ##Incorpora ficha del bot a el tablero
    fila = 5
    if win == False:
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

    tablero_bytes = pickle.dumps(tablero)
    conexion.send(tablero_bytes)  #Mandamos tablero actualizado al cliente
    print("Tablero enviado al cliente")
    

    #Checkeamos ganador
    if win == True:
        mensaje = '3'
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


    
    if check_win(tablero, 'M'):
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

    else:
        mensaje = '5'
        conexion.send(mensaje.encode('utf-8'))


    

    
    
    
'''   
    mensaje = "Hola, te saludo desde el servidor!"
    mensaje_bytes = mensaje.encode('utf-8')
    conexion.send(mensaje_bytes)
    
    
    mensaje2 = "Hola, servidor go!"
    mi_socket2.sendto(mensaje2.encode('utf-8'), ('127.0.0.1', 1234))
    
    data, address = mi_socket2.recvfrom(1024)
    print(f"Mensaje recibido de {address}: {data.decode('utf-8')}")
    
    conexion.close()
    mi_socket2.close()
'''
    

    
