
import socket

def Main():
        host = '127.0.0.1'#'200.14.84.235'
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((host,port))

        #message = input(" -> ")
        message = "00010sinit_dv__"

        while message != 'q':
                #print (message)
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()


                #print ('Received from server: ' + data)
                data2 = "".join(data)
                if data2[5:10] == "_dv__":#"00012sinitOK    z":
                    number = int(data2[0:5])
                    respuesta = data2[10:number+5-1]
                    number2 = int(data2[number+5-1:number+5])
                    number2 = number2 + 1
                    #print (data)
                    #print (number)
                    #print (respuesta)
                    message = "000" + str(number) + "_dv__" + respuesta + str(number2)
                else:
                    message = "00010sinit_dv__"
                #message= input(" -> ")

        mySocket.close()

if __name__ == '__main__':
    Main()

#Cuando es llamado el servicio, descompone la data para dejar solo el contenido importante
#El servicio recibe un hola mas un numero, luego le suma uno a ese numero y responde
