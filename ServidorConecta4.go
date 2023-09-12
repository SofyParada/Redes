package main

import (
	
	"fmt"
	"net"
	"os"
    "math/rand"
    "strconv"
    
)

func main() {
    // Dirección en la que el servidor Go escuchará
    serverAddr, err := net.ResolveUDPAddr("udp", "0.0.0.0:1234")
    if err != nil {
        fmt.Println("Error al resolver la dirección del servidor:", err)
        os.Exit(1)
        
    }

    
    tablero := [6][6]string{{"0","0","0","0","0","0"},{"0","0","0","0","0","0"},{"0","0","0","0","0","0"},{"0","0","0","0","0","0"},{"0","0","0","0","0","0"},{"0","0","0","0","0","0"}}

    
    // Crear una conexión UDP
    conn, err := net.ListenUDP("udp", serverAddr)//escuchar lo enviado por el servidor intermediario
    if err != nil {
        fmt.Println("Error al crear la conexión UDP:", err)
            os.Exit(1)
    }
    defer conn.Close()

    fmt.Println("Servidor Go escuchando en 0.0.0.0:1234")


        
    buffer := make([]byte, 1024)
    
    // Leer datos del servidor Python
    n, addr, err := conn.ReadFromUDP(buffer) //recibir los datos del servidor intermeiario
    if err != nil {
        fmt.Println("Error al leer datos del servidor Python:", err)
        return
    }

    // Procesar y mostrar los datos recibidos
    data := string(buffer[:n])
    fmt.Printf("Datos recibidos de %s: %s\n", addr, data)

            
    if data == "b'1'"{
        Mensaje := "OK"
        MensajeBytes := []byte(Mensaje)
        _, err = conn.WriteToUDP(MensajeBytes, addr) //mensaje enviado al sevidor intermediario 
        if err != nil {
            fmt.Println("Error al enviar datos al servidor:", err)
            return
        }
        fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)
        //var FilaAle int
        PuertoMin := 8000
        PuertoMax := 65535
        direccion := "127.0.0.1"
        for puerto := PuertoMin; puerto <= PuertoMax; puerto++{
            destino := fmt.Sprintf("%s:%d", direccion, puerto )
            Conexion, err := net.ResolveUDPAddr("udp", destino)
            if err != nil {
                fmt.Println("Error al resolver la dirección del servidor:", err)
                 os.Exit(1)
        
            }
            var fila int 
            fila = 5
           
            conn, err := net.ListenUDP("udp", Conexion)//escuchar lo enviado por el servidor intermediario
            if err != nil {
                fmt.Println("Error al crear la conexión UDP:", err)
                os.Exit(1)
            }
            defer conn.Close()

            fmt.Println("Servidor Go escuchando en ", destino)

            buffer := make([]byte, 1024)
    
            // Leer datos del servidor Python
            n, addr, err := conn.ReadFromUDP(buffer) //recibir los datos del servidor intermeiario
            if err != nil {
                fmt.Println("Error al leer datos del servidor Python:", err)
                return
            }

            // Procesar y mostrar los datos recibidos
            data := string(buffer[:n])
            fmt.Printf("Datos recibidos de %s: %s\n", addr, data)

            //if data == "b'6'" || data == "b'5'"|| data == "b'4'"|| data == "b'3'"|| data == "b'1'"{}
            if data == "b'1'"{
                for tablero[fila][0] != "0" && fila >= 0{
                    fila = fila - 1
                }
                tablero[fila][0] = "A"

            }else if data == "b'2'"{
                for tablero[fila][1] != "0" && fila >= 0{
                    fila = fila - 1
                }
                tablero[fila][1] = "A"
            }else if data == "b'3'"{
                for tablero[fila][2] != "0" && fila >= 0{
                    fila = fila - 1
                }
                tablero[fila][2] = "A"
            }else if data == "b'4'"{
                for tablero[fila][3] != "0" && fila >= 0{
                    fila = fila - 1
                }
                tablero[fila][3] = "A"
            }else if data == "b'5'"{
                for tablero[fila][4] != "0" && fila >= 0{
                    fila = fila - 1
                }
                tablero[fila][4] = "A"
            }else if data == "b'6'"{
                for tablero[fila][5] != "0" && fila >= 0{
                    fila = fila - 1
                }
                tablero[fila][5] = "A"
            }
            i := 0
            for i == 0{
                ColumnaAle := rand.Intn(6)
                fila2 := 5
                if ColumnaAle == 0{
                    for tablero[fila2][0] != "0" && fila2 >= 0{
                        fila = fila - 1
                    }
                    if fila2 >= 0{
                        tablero[fila2][0] = "M"
                        i = 1
                        ColumnaAle_str := strconv.Itoa(ColumnaAle)
                        ColumnaAle_bytes :=  []byte(ColumnaAle_str)
                        _, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario 
                        if err != nil {
                            fmt.Println("Error al enviar datos al servidor:", err)
                            return
                        }
                        fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)
                        
                    }

                }else if ColumnaAle == 1{
                    for tablero[fila2][01] != "0" && fila2 >= 0{
                        fila = fila - 1
                    }
                    if fila2 >= 0{
                        tablero[fila2][01] = "M"
                        i = 1
                        ColumnaAle_str := strconv.Itoa(ColumnaAle)
                        ColumnaAle_bytes :=  []byte(ColumnaAle_str)
                        _, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario 
                        if err != nil {
                            fmt.Println("Error al enviar datos al servidor:", err)
                            return
                        }
                        fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)
                        
                    }

                }else if ColumnaAle == 2{
                    for tablero[fila2][2] != "0" && fila2 >= 0{
                        fila = fila - 1
                    }
                    if fila2 >= 0{
                        tablero[fila2][2] = "M"
                        i = 1
                        ColumnaAle_str := strconv.Itoa(ColumnaAle)
                        ColumnaAle_bytes :=  []byte(ColumnaAle_str)
                        _, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario 
                        if err != nil {
                            fmt.Println("Error al enviar datos al servidor:", err)
                            return
                        }
                        fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)
                        
                    }

                }else if ColumnaAle == 3{
                    for tablero[fila2][3] != "0" && fila2 >= 0{
                        fila = fila - 1
                    }
                    if fila2 >= 0{
                        tablero[fila2][3] = "M"
                        i = 1
                        ColumnaAle_str := strconv.Itoa(ColumnaAle)
                        ColumnaAle_bytes :=  []byte(ColumnaAle_str)
                        _, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario 
                        if err != nil {
                            fmt.Println("Error al enviar datos al servidor:", err)
                            return
                        }
                        fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)
                        
                    }

                }else if ColumnaAle == 4{
                    for tablero[fila2][4] != "0" && fila2 >= 0{
                        fila = fila - 1
                    }
                    if fila2 >= 0{
                        tablero[fila2][4] = "M"
                        i = 1
                        ColumnaAle_str := strconv.Itoa(ColumnaAle)
                        ColumnaAle_bytes :=  []byte(ColumnaAle_str)
                        _, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario 
                        if err != nil {
                            fmt.Println("Error al enviar datos al servidor:", err)
                            return
                        }
                        fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)
                        
                    }

                }else if ColumnaAle == 5{
                    for tablero[fila2][5] != "0" && fila2 >= 0{
                        fila = fila - 1
                    }
                    if fila2 >= 0{
                        tablero[fila2][5] = "M"
                        i = 1
                        ColumnaAle_str := strconv.Itoa(ColumnaAle)
                        ColumnaAle_bytes :=  []byte(ColumnaAle_str)
                        _, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario 
                        if err != nil {
                            fmt.Println("Error al enviar datos al servidor:", err)
                            return
                        }
                        fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)
                        
                    }

                }
                
            }

            


        }
    }else if data == "b'2'"{
        Mensaje := "NO"
        MensajeBytes := []byte(Mensaje)
        _, err = conn.WriteToUDP(MensajeBytes, addr)
        if err != nil {
            fmt.Println("Error al enviar datos al servidor:", err)
            return
        }
        fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)

        }

}

           
            

    

        // Rutina del cliente para enviar datos
       // message := "¡Hola, servidor de python!"
    
        //messageBytes := []byte(message)
    
        //_, err = conn.WriteToUDP(messageBytes, addr)
        //if err != nil {
            //fmt.Println("Error al enviar datos al servidor:", err)
            //return
        //}
        //fmt.Printf("Datos enviados al servidor: %s\n", message)   
    
    
    
