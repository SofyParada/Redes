import socket

mi_socket = socket.socket()
mi_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mi_socket.bind( (socket.gethostname(), 8000) )
mi_socket.listen(5)



while True:
    conexion, addr = mi_socket.accept()
    print("Nueva conexion establecida")
    print(addr)
    
    peticion = conexion.recv(1024)
    print(peticion)
    
    
    mensaje = "Hola, te saludo desde el servidor!"
    mensaje_bytes = mensaje.encode('utf-8')
    conexion.send(mensaje_bytes)
    
    mensaje2 = "Hola, servidor go!"
    mi_socket.sendto(mensaje2.encode('utf-8'), (socket.gethostname(), 8000))
    
    
    conexion.close()
