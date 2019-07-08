
import socket

def Main():
        host = '127.0.0.1'#'200.14.84.235'
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((host,port))


        menu = """Bienvenido al Restaurant Tan Dao Vien
        elija una opcion:
        1.-Agregar Menu
        2.-Ver Menús
        3.-Delivery
        4.-Ver ventas
        5.-Salir
        """
        print(menu)
        opcion = int(input("Escriba aqui su opcion: "))

        if opcion is 1:
            print("Usted va a agregar un menu")
            menu = str(input("Menú:"))
            message = "00010_mn2_" + menu

        elif opcion is 2:

            message = "00010_mn__hola1"

        elif opcion is 3:

            print("Para Delivery, ingrese los siguientes datos: ")
            nombre = input(" Nombre: ")
            apellido = input(" Apellido: ")
            rut = input(" Rut: ")
            telefono = input(" Telefono: ")
            tipo_menu = input(" Numero del Menú: ")
            direccion = input(" Dirección: ")
            comuna = input(" Comuna: ")
            message = "00010_dv__"+str(nombre)+ "," +str(apellido)+ "," +str(rut)+ "," +str(telefono)+ "," +str(tipo_menu)+ "," +str(direccion)+ "," +str(comuna)#input(" -> ")


        elif opcion is 4:

            print("Ventas: ")
            message = "00010_vt__hola1"

        elif opcion is 5:
            print("Hasta pronto")
            message = "q"

        else:
            print("Opcion invalida , reingrese ")
            message = "q"

        data2 = ""
        #message = "00010_mn2_comida"
        while message != 'q':
                #print (message)
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                data2 = "".join(data)
                #print(data2[5:12])
                if data2[5:10] == '_mn__':
                    number = int(data2[0:5])
                    respuesta = data2[12:number+5]
                    respuestas = respuesta.split(",")
                    respuestas.pop()
                    print ("Menús Disponibles:")
                    for respuesta in respuestas:
                        print ("-" + respuesta)
                    break


                if data2[5:10] == '_dv__':
                    number = int(data2[0:5])
                    respuesta = data2[12:number+5]
                    #respuestas = respuesta.split(",")
                    print(respuesta)
                    #print ("Menús Disponibles:")
                    #for respuesta in respuestas:
                        #print ("-" + respuesta)
                    if respuesta == "OK":
                        print ("Delivery agregado a la lista")
                    else:
                        print ("Error con el menú")
                    break

                if data2[5:10] == '_vt__':
                    number = int(data2[0:5])
                    respuesta = data2[12:number+5]
                    respuestas = respuesta.split("|")
                    lista = []
                    for resp in respuestas:
                        lista.append(resp.split(","))
                    lista.pop()
                    #respuestas.pop()
                    #print ("Menús Disponibles:")
                    #for respuesta in respuestas:
                        #print ("-" + respuesta)
                    print ("-------------------------------------")
                    for objeto in lista:
                        print("ID: " + objeto[0])
                        print("Nombre: " + objeto[1])
                        print("Apellido: " + objeto[2])
                        print("Rut: " + objeto[3])
                        print("Telefono: " + objeto[4])
                        print("Menú: " + objeto[5])
                        print("Tipo de Menú: " + objeto[6])
                        print("Monto: " + objeto[7])
                        print("Fecha: " + objeto[8])
                        print ("-------------------------------------")

                    break

                if data2[5:10] == '_mn2_':
                    number = int(data2[0:5])
                    respuesta = data2[12:number+5]
                    #respuestas = respuesta.split(",")
                    #respuestas.pop()
                    #print ("Menús Disponibles:")
                    #for respuesta in respuestas:
                        #print ("-" + respuesta)
                    if respuesta == "OK":
                        print ("Menú agregado a la lista")
                    else:
                        print ("Error con el menú")
                    break


                print ('Received from server: ' + data)
                message = input(" -> ")#"00010_dv__hola3"


        mySocket.close()

if __name__ == '__main__':
    Main()





#El usuario envia el message del principio, luego recibe el numero del final mas 1
#Un vez que recibe respuesta termina
