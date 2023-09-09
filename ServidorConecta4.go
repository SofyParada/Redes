package main

import (
    "fmt"
    "net"
)

func main() {
    // Dirección en la que el servidor Go escuchará
    serverAddr, err := net.ResolveUDPAddr("udp", "192.168.0.8:8000")
    if err != nil {
        fmt.Println("Error al resolver la dirección del servidor:", err)
        return
    }

    // Crear una conexión UDP
    conexion, err := net.ListenUDP("udp", serverAddr)
    if err != nil {
        fmt.Println("Error al crear la conexión UDP:", err)
        return
    }
    defer conexion.Close()

    fmt.Println("Servidor Go escuchando en 192.168.0.8:8000")

    for {
        // Leer datos del servidor Python
        buffer := make([]byte, 1024)
        _, addr, err := conexion.ReadFromUDP(buffer)
        if err != nil {
            fmt.Println("Error al leer datos del servidor Python:", err)
            return
        }

        // Procesar y mostrar los datos recibidos
        data := string(buffer)
        fmt.Printf("Datos recibidos de %s: %s\n", addr, data)
    }
}
