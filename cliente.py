import socket

mi_socket = socket.socket()
mi_socket.connect( (socket.gethostname(), 8000) )

mensaje = "Hola, te saludo desde el cliente!"
mensaje_bytes = mensaje.encode('utf-8')

mi_socket.send(mensaje_bytes)
respuesta = mi_socket.recv(1024)

print(respuesta)
mi_socket.close()

