package main

import (
	"fmt"
	"math/rand"
	"net"
	"os"
	"strconv"
)

func main() {
	// Dirección en la que el servidor Go escuchará
	serverAddr, err := net.ResolveUDPAddr("udp", "0.0.0.0:1234")
	if err != nil {
		fmt.Println("Error al resolver la dirección del servidor:", err)
		os.Exit(1)

	}

	tablero := [6][6]string{{"0", "0", "0", "0", "0", "0"}, {"0", "0", "0", "0", "0", "0"}, {"0", "0", "0", "0", "0", "0"}, {"0", "0", "0", "0", "0", "0"}, {"0", "0", "0", "0", "0", "0"}, {"0", "0", "0", "0", "0", "0"}}

	// Crear una conexión UDP
	conn, err := net.ListenUDP("udp", serverAddr) //escuchar lo enviado por el servidor intermediario
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

	if data == "1" {
		Mensaje := "OK"
		MensajeBytes := []byte(Mensaje)
		_, err = conn.WriteToUDP(MensajeBytes, addr) //mensaje enviado al sevidor intermediario
		if err != nil {
			fmt.Println("Error al enviar datos al servidor:", err)
			return
		}
		fmt.Printf("Datos enviados al servidor: %s\n", Mensaje)

		flag := false
		i := 0
		for flag == false { // While para que no se cierre go

			//var FilaAle int
			PuertoMin := 8000
			PuertoMax := 65535
			Puerto := rand.Intn(PuertoMax-PuertoMin) + PuertoMin //Randomiza puerto
			fmt.Printf("Puerto a utilizar es :%d\n", Puerto)
			direccion := "127.0.0.1"

			destino := fmt.Sprintf("%s:%d", direccion, Puerto) //Mandamos puerto a intermediario para poder conectarse
			MensajeBytes = []byte(strconv.Itoa(Puerto))
			_, err = conn.WriteToUDP(MensajeBytes, addr)
			if err != nil {
				fmt.Println("Error al enviar datos al servidor:", err)
				return
			}
			fmt.Printf("Datos enviados al servidor: %d\n", Puerto)

			Conexion, err := net.ResolveUDPAddr("udp", destino)
			if err != nil {
				fmt.Println("Error al resolver la dirección del servidor:", err)
				os.Exit(1)

			}

			var fila int
			fila = 5

			conn, err := net.ListenUDP("udp", Conexion) //escuchar lo enviado por el servidor intermediario
			if err != nil {
				fmt.Println("Error al crear la conexión UDP:", err)
				os.Exit(1)
			}
			defer conn.Close()

			fmt.Println("Servidor Go escuchando en ", destino)

			jugadacliente := make([]byte, 1024)

			// Leer datos del servidor Python
			n, addr, err := conn.ReadFromUDP(jugadacliente) //Recibir jugada del cliente
			if err != nil {
				fmt.Println("Error al leer datos del servidor Python:", err)
				return
			}

			// Procesar y mostrar los datos recibidos
			cliente := string(jugadacliente[:n])
			fmt.Printf("Datos recibido de %s: %s\n", addr, cliente)

			if cliente == "cerrar" { //Si el cliente quiere terminar el juego, se sale del loop
				break
			}

			if cliente == "1" {
				for tablero[fila][0] != "0" && fila >= 0 {
					fila = fila - 1
				}
				tablero[fila][0] = "A"
				fmt.Println("Entro a 1")

			} else if cliente == "2" {
				for tablero[fila][1] != "0" && fila >= 0 {
					fila = fila - 1
				}
				tablero[fila][1] = "A"

			} else if cliente == "3" {
				for tablero[fila][2] != "0" && fila >= 0 {
					fila = fila - 1
				}
				tablero[fila][2] = "A"
				fmt.Println("Entro a 3")

			} else if cliente == "4" {
				for tablero[fila][3] != "0" && fila >= 0 {
					fila = fila - 1
				}
				tablero[fila][3] = "A"

			} else if cliente == "5" {
				for tablero[fila][4] != "0" && fila >= 0 {
					fila = fila - 1
				}
				tablero[fila][4] = "A"

			} else if cliente == "6" {
				for tablero[fila][5] != "0" && fila >= 0 {
					fila = fila - 1
				}
				tablero[fila][5] = "A"

			}
			i = 0
			for i == 0 {
				ColumnaAle := rand.Intn(6)
				fmt.Printf("La columa elegida fue: %d", ColumnaAle)
				fila2 := 5
				if ColumnaAle == 0 {
					for tablero[fila2][0] != "0" && fila2 >= 0 {
						fila2 = fila2 - 1
					}
					if fila2 >= 0 {
						tablero[fila2][0] = "M"
						i = 1
						ColumnaAle_str := strconv.Itoa(ColumnaAle)
						ColumnaAle_bytes := []byte(ColumnaAle_str)
						_, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario
						if err != nil {
							fmt.Println("Error al enviar datos al servidor:", err)
							return
						}
						fmt.Printf("Datos enviados al servidor: %s\n", ColumnaAle_str)

					}

				} else if ColumnaAle == 1 {
					for tablero[fila2][1] != "0" && fila2 >= 0 {
						fila2 = fila2 - 1
					}
					if fila2 >= 0 {
						tablero[fila2][1] = "M"
						i = 1
						ColumnaAle_str := strconv.Itoa(ColumnaAle)
						ColumnaAle_bytes := []byte(ColumnaAle_str)
						_, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario
						if err != nil {
							fmt.Println("Error al enviar datos al servidor:", err)
							return
						}
						fmt.Printf("Datos enviados al servidor: %s\n", ColumnaAle_str)

					}

				} else if ColumnaAle == 2 {
					for tablero[fila2][2] != "0" && fila2 >= 0 {
						fila2 = fila2 - 1
					}
					if fila2 >= 0 {
						tablero[fila2][2] = "M"
						i = 1
						ColumnaAle_str := strconv.Itoa(ColumnaAle)
						ColumnaAle_bytes := []byte(ColumnaAle_str)
						_, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario
						if err != nil {
							fmt.Println("Error al enviar datos al servidor:", err)
							return
						}
						fmt.Printf("Datos enviados al servidor: %s\n", ColumnaAle_str)

					}

				} else if ColumnaAle == 3 {
					for tablero[fila2][3] != "0" && fila2 >= 0 {
						fila2 = fila2 - 1
					}
					if fila2 >= 0 {
						tablero[fila2][3] = "M"
						i = 1
						ColumnaAle_str := strconv.Itoa(ColumnaAle)
						ColumnaAle_bytes := []byte(ColumnaAle_str)
						_, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario
						if err != nil {
							fmt.Println("Error al enviar datos al servidor:", err)
							return
						}
						fmt.Printf("Datos enviados al servidor: %s\n", ColumnaAle_str)

					}

				} else if ColumnaAle == 4 {
					for tablero[fila2][4] != "0" && fila2 >= 0 {
						fila2 = fila2 - 1
					}
					if fila2 >= 0 {
						tablero[fila2][4] = "M"
						i = 1
						ColumnaAle_str := strconv.Itoa(ColumnaAle)
						ColumnaAle_bytes := []byte(ColumnaAle_str)
						_, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario
						if err != nil {
							fmt.Println("Error al enviar datos al servidor:", err)
							return
						}
						fmt.Printf("Datos enviados al servidor: %s\n", ColumnaAle_str)

					}

				} else if ColumnaAle == 5 {
					for tablero[fila2][5] != "0" && fila2 >= 0 {
						fila2 = fila2 - 1
					}
					if fila2 >= 0 {
						tablero[fila2][5] = "M"
						i = 1
						ColumnaAle_str := strconv.Itoa(ColumnaAle)
						ColumnaAle_bytes := []byte(ColumnaAle_str)
						_, err = conn.WriteToUDP(ColumnaAle_bytes, addr) //mensaje enviado al sevidor intermediario
						if err != nil {
							fmt.Println("Error al enviar datos al servidor:", err)
							return
						}
						fmt.Printf("Datos enviados al servidor: %s\n", ColumnaAle_str)

					}
				}
			}
		}
	}

	if data == "2" {
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
