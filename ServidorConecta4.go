package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    // Dirección en la que el servidor Go escuchará
    serverAddr, err := net.ResolveUDPAddr("udp", "0.0.0.0:1234")
    if err != nil {
        fmt.Println("Error al resolver la dirección del servidor:", err)
        os.Exit(1)
        
    }

    // Crear una conexión UDP
    conn, err := net.ListenUDP("udp", serverAddr)
    if err != nil {
        fmt.Println("Error al crear la conexión UDP:", err)
        os.Exit(1)
    }
    defer conn.Close()

    fmt.Println("Servidor Go escuchando en 0.0.0.0:1234")


    
    buffer := make([]byte, 1024)
    for {
        // Leer datos del servidor Python
        n, addr, err := conn.ReadFromUDP(buffer)
        if err != nil {
            fmt.Println("Error al leer datos del servidor Python:", err)
            continue
        }

        // Procesar y mostrar los datos recibidos
        data := string(buffer[:n])
        fmt.Printf("Datos recibidos de %s: %s\n", addr, data)

        print(data)
        if data == "b'1'"{
            Mensaje := "OK"
            MensajeBytes := []byte(Mensaje)
            _, err = conn.WriteToUDP(MensajeBytes, addr)
            if err != nil {
                fmt.Println("Error al enviar datos al servidor:", err)
                continue
            }
            fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)


        }else{
            Mensaje := "NO"
            MensajeBytes := []byte(Mensaje)
            _, err = conn.WriteToUDP(MensajeBytes, addr)
            if err != nil {
                fmt.Println("Error al enviar datos al servidor:", err)
                continue
            }
            fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)

        }


        // Rutina del cliente para enviar datos
        message := "¡Hola, servidor de python!"
    
        messageBytes := []byte(message)
    
        _, err = conn.WriteToUDP(messageBytes, addr)
        if err != nil {
            fmt.Println("Error al enviar datos al servidor:", err)
            continue
        }
        fmt.Printf("Datos enviados al servidor: %s\n", message)   
    }
    
    

    
}
