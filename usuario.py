
import socket

def Main():
        host = '127.0.0.1'#'200.14.84.235'
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((host,port))

        message = "00010_dv__hola1000"#input(" -> ")
        data2 = ""

        while message != 'q':
                #print (message)
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                data2 = "".join(data)
                #print(data2[5:12])
                if data2[5:12] == '_dv__OK':
                    number = int(data2[0:5])
                    respuesta = data2[12:number+5]
                    print (respuesta)
                    break
                print ('Received from server: ' + data)
                message = input(" -> ")#"00010_dv__hola3"


        mySocket.close()

if __name__ == '__main__':
    Main()





#El usuario envia el message del principio, luego recibe el numero del final mas 1
#Un vez que recibe respuesta termina
