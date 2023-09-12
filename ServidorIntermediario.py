import socket
import numpy as np
import ast

mi_socket = socket.socket()
mi_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mi_socket.bind( (socket.gethostname(), 8000) )
mi_socket.listen(5)


while True:
    conexion, addr = mi_socket.accept()
    print("Nueva conexion establecida")
    print(addr)
    
    peticion = str(conexion.recv(1024)) #mensaje recibido del cliente
    print("mensaje recibido del cliente: ", peticion)
    
    
    mi_socket2.sendto(peticion.encode('utf-8'), ('127.0.0.1', 1234))
    print("Mensaje enviado al Servidor Conecta 4: ",peticion)
        
    data, address = mi_socket2.recvfrom(1024)
    print(f"Mensaje recibido de {address}: {data.decode('utf-8')}")
        
    Mensaje = str(data.decode('utf-8')) #parece que hice una wea rara aquí, pero funciona jiji
    Mensaje_bytes = Mensaje.encode('utf-8')
    conexion.send(Mensaje_bytes)
    print("Mensaje enviado al cliente: ", Mensaje)
        
    tablero_bytes= conexion.recv(1024)
    tablero = tablero_bytes.decode('utf-16le')
    print({tablero})
     
    tablero = tablero[:6 * 6] #chatgpt jiji
    tablero = np.array(list(tablero)).reshape(6, 6)
    
    
    #tablero = [tablero1,tablero2,tablero3,tablero4,tablero5,tablero6]
    
    '''
    tablero1 = np.fromstring((tablero[:6]), dtype=str, sep='')
    tablero2 = np.fromstring((tablero[6:11]), dtype=str, sep='')
    tablero3 = np.fromstring((tablero[11:16]), dtype=str, sep='')
    tablero4 = np.fromstring((tablero[16:21]), dtype=str, sep='')
    tablero5 = np.fromstring((tablero[21:26]), dtype=str, sep='')
    tablero6 = np.fromstring((tablero[26:]), dtype=str, sep='')
    
    tablero = np.array([tablero1, tablero2,tablero3, tablero4, tablero5, tablero6])
    '''
   
    
    
    print(tablero)
    
    

        
    
    conexion.close()
    mi_socket2.close()
    mi_socket.close()
    
    
    
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
    

