
import random
import socket
import psycopg2

conn = psycopg2.connect("dbname=arquidb")
cur = conn.cursor()

def Main():
        host = '127.0.0.1'#'200.14.84.235'
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((host,port))

        #message = input(" -> ")
        message = "00010sinit_mn2_"

        while message != 'q':
                #print (message)
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                #print ('Received from server: ' + data)
                data2 = "".join(data)
                if data2[5:10] == "_mn2_":
                    number = int(data2[0:5])
                    respuesta = data2[10:number+5]
                    print (respuesta)
                    if respuesta!="":
                        numero = str(random.randrange(10,1000))
                        sql = "insert into public.menu values (" + numero
                        sql = sql + ", '" + str(respuesta)
                        sql = sql + "' , '2019-07-08');"
                        print (sql)
                        cur.execute(sql)
                        conn.commit()
                        message = "000" + str(10) + "_mn2_" + "OK"
                    else:
                        message = "000" + str(10) + "_mn2_" + "NK"
                else:
                    message = "00010sinit_mn2_"
                #message= input(" -> ")

        mySocket.close()

if __name__ == '__main__':
    Main()

#Cuando es llamado el servicio, descompone la data para dejar solo el contenido importante
#El servicio recibe un hola mas un numero, luego le suma uno a ese numero y responde
