
import socket

def Main():
        host = '200.14.84.235'
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((host,port))

        #message = input(" -> ")
        message = "00010sinit_mn"

        while message != 'q':
                #print (message)
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()


                print ('Received from server: ' + data)
                data2 = "".join(data)
                if data2 == "00000":#"00012sinitOK    z":
                    print (data)
                    message = "00001z"
                message= input(" -> ")

        mySocket.close()

if __name__ == '__main__':
    Main()
