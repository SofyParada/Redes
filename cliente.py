import socket
import numpy as np
import pickle

mi_socket = socket.socket()
mi_socket.connect( (socket.gethostname(), 8000) )

print("- - - - - - - - Bienvenido al Juego - - - - - - - -")
Seleccion =input("- Seleccione una opción\n1-Jugar\n2-Salir\n")

if Seleccion == '1': #arreglar los if por ok y no
    Seleccion_bytes = Seleccion.encode('utf-8')
    mi_socket.send(Seleccion_bytes)
    

    print("- - - - - - - - Comienza el Juego - - - - - - - -")
    
    tablero = np.array([['0','0','0','0','0','0'], 
                        ['0','0','0','0','0','0'], 
                        ['0','0','0','0','0','0'],
                        ['0','0','0','0','0','0'],
                        ['0','0','0','0','0','0'],
                        ['0','0','0','0','0','0']])
    print("Tablero inicial:\n",tablero)
    
    #Las fichas azules seran del jugador y su variable sera A
    #Las fichas moradas seran del BOT y su variables sera M
    #Supongamos que el jugador va a empezar a jugar
    
    
    #while
    columna = 0
    flag = False

    #Comienza while loop para que no se pierda la conexion despues de una iteracion
    while flag == False: 

        while flag == False:  #A partir del input, reviso si jugada es valida segun tablero
            fila = 5
            jugada = input("En que columna quieres colocar tu ficha: ")
            if jugada == '1':
                
                while tablero[fila][0] != '0' and fila >= 0:
                    fila -= 1
                if fila >= 0:
                    tablero[fila][0] = 'A'
                    flag = True
                    
                else:
                    print("Esta columna esta completa de filas, eliga otra: ")
                    Flag = False
                
            elif jugada == '2':
                while tablero[fila][1] != '0' and fila >= 0:
                    fila -= 1
                if fila >= 0:
                    tablero[fila][1] = 'A'
                    flag = True
                else:
                    print("Esta columna esta completa de fillas, eliga otra: ")
                    flag = False
                
            elif jugada == '3':
                while tablero[fila][2] != '0' and fila >= 0:
                    fila -= 1
                    
                if fila >= 0:
                    tablero[fila][2] = 'A'
                    flag = True
                else:
                    print("Esta columna esta completa de fillas, eliga otra: ")
                    flag = False
                
            elif jugada == '4':
                while tablero[fila][3] != '0' and fila >= 0:
                    fila -= 1
                    
                if fila >= 0:
                    tablero[fila][3] = 'A'
                    flag = True
                else:
                    print("Esta columna esta completa de fillas, eliga otra: ")
                    flag = False
                
            elif jugada == '5':
                while tablero[fila][4] != '0' and fila >= 0:
                    fila -= 1
                    
                if fila >= 0:
                    tablero[fila][4] = 'A'
                    flag = True
                else:
                    print("Esta columna esta completa de fillas, eliga otra: ")
                    flag = False
                
            elif jugada == '6':
                while tablero[fila][5] != '0' and fila >= 0:
                    fila -= 1
                    
                if fila >= 0:
                    tablero[fila][5] = 'A'
                    flag = True
                else:
                    print("Esta columna esta completa de fillas, eliga otra: ")
                    flag = False
                    
            else:
                print("Este numero no esta dentro del rango de la tabla, porfavor elija otra")
                flag = False
        

        #Se toma la jugada y se manda a el intermediario 

        fila_str = str(jugada)
        fila_bytes = fila_str.encode('utf-8')  #Jugador manda columna a intermediario
        mi_socket.send(fila_bytes)
        

        tablero_bytes = (mi_socket.recv(4096))  #Cliente recibe tablero actualizado
        newtablero = pickle.loads(tablero_bytes) #Descomprime tablero
        
        print("El nuevo tablero es:\n")
        print(newtablero)

        mensaje = mi_socket.recv(1024).decode('utf-8')  #Mensaje que establece si el juego termina, segun senal recibida

        if mensaje == '3':
            print("Termina el juego, gana el cliente")
            End = "cerrar"
            End_bytes = End.encode('utf-8')
            mi_socket.close()
            flag = False
            break


        if mensaje == '4':
            print("Termina el juego, gana el bot")
            End = "cerrar"
            End_bytes = End.encode('utf-8')
            mi_socket.close()
            flag = False
            break

        if mensaje == '5':
            print("No hay mas espacio para jugar, hay un empate, termina el juego")
            End = "cerrar"
            End_bytes = End.encode('utf-8')
            mi_socket.close()
            flag = False
            break

        while flag == True:  #En cada turno pregunta si quiere seguir jugando o terminar el proceso
            Continue = input("Quiere seguir jugando? Si/No\n")
            if Continue == "Si" or Continue == "si":
                flag = False
            if Continue == "No" or Continue == "no":
                Seleccion = "cerrar"
                break
            

    if flag == True:  #Termina procesos
        End = "cerrar"
        End_bytes = End.encode('utf-8')
        mi_socket.send(End_bytes)
        mi_socket.close()
        exit(1)
    
    
if Seleccion == "cerrar":  #Ante la palabra cerrar, termina procesos
    
    Seleccion_bytes = Seleccion.encode('utf-8')
    mi_socket.send(Seleccion_bytes)
    
    respuesta = str(mi_socket.recv(1024))
    print("Respuesta de disponibilidad: ", respuesta)
    mi_socket.close()    

