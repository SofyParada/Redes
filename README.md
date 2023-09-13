Benjamin Gutierrez 202004621-2  Sofía Parada hormazábal 202004671-9

Instrucciones de ejecucion:

El orden de iniciar los archivos debe ser ServidorConecta4.go -> ServidorIntermediario.py -> cliente.py

Se recomienda realizar esto en Visual Studio Code, ingresando los archivos a una misma carpeta.
Para ejecutar el .go, se debe escribir en una terminal powershell go run ServidorConecta4.go,
luego iniciar el servidorintermediario y finalmente el cliente, el cual indicara por la consola una conexion exitosa
y dara las indicaciones para empezar el juego

En el primer turno se debe elegir una columna en donde ingresar la ficha del cliente,
en los siguientes turnos se le indicara el tablero actualizado y una pregunta de si desea continuar jugando,
esta se debe responder con un Si/si o un No/no.
Las siguientes iteraciones son iguales.
Cuando haya un ganador se indicara por la consola y se terminara la ejecucion.


Librerias extras:

Se utiliza la libreria numpy para crear el tablero
Se utiliza libreria pickle para comprimir tablero en bytes y poder enviarlo al cliente.
