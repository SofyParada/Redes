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
    mi_socket2.sendto(mensaje2.encode('utf-8'), ('127.0.0.1', 1234))
    
    data, address = mi_socket2.recvfrom(1024)
    print(f"Mensaje recibido de {address}: {data.decode('utf-8')}")
    
    conexion.close()
    mi_socket2.close()
    

    
