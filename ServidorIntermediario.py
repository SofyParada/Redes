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
    print("Esperando segunda peticion")
    peticion2 = conexion.recv(1024)
    jugada = peticion2.decode('utf-8')
    

    

    if jugada == '1':
        
        while tablero[fila][0] != '0' and fila >= 0:
            fila -= 1
        if fila >= 0:
            print("Entro en 1")
            tablero[fila][0] = 'A'
            
    elif jugada == '2':
        while tablero[fila][1] != '0' and fila >= 0:
            fila -= 1
        if fila >= 0:
            print("Entro en 2")
            tablero[fila][1] = 'A'
        
    elif jugada == '3':
        while tablero[fila][2] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            print("Entro en 3")
            tablero[fila][2] = 'A'
        
    elif jugada == '4':
        while tablero[fila][3] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            print("Entro en 4")
            tablero[fila][3] = 'A'
        
    elif jugada == '5':
        while tablero[fila][4] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            print("Entro en 5")
            tablero[fila][4] = 'A'

    elif jugada == '6':
        while tablero[fila][5] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            print("Entro en 6")
            tablero[fila][5] = 'A'

    

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

    if jugadago== '0':
        
        while tablero[fila][0] != '0' and fila >= 0:
            fila -= 1
        if fila >= 0:
            print("Entro en 1")
            tablero[fila][0] = 'M'
            
    elif jugadago == '1':
        while tablero[fila][1] != '0' and fila >= 0:
            fila -= 1
        if fila >= 0:
            print("Entro en 2")
            tablero[fila][1] = 'M'
        
    elif jugadago == '2':
        while tablero[fila][2] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            print("Entro en 3")
            tablero[fila][2] = 'M'
        
    elif jugadago == '3':
        while tablero[fila][3] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            print("Entro en 4")
            tablero[fila][3] = 'M'
        
    elif jugadago == '4':
        while tablero[fila][4] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            print("Entro en 5")
            tablero[fila][4] = 'M'

    elif jugadago == '5':
        while tablero[fila][5] != '0' and fila >= 0:
            fila -= 1
            
        if fila >= 0:
            print("Entro en 6")
            tablero[fila][5] = 'M'


    print(tablero)

    tablero_bytes = pickle.dumps(tablero)
    conexion.send(tablero_bytes)  #Mandamos tablero actualizado al cliente
    print("Mensaje enviado al cliente:")

    
    

    
    
    
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
    

    
