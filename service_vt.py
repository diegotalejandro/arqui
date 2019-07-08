
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
        message = "00010sinit_mn__"

        while message != 'q':
                #print (message)
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                #print ('Received from server: ' + data)
                data2 = "".join(data)
                if data2[5:10] == "_vt__":
                    sql = "select * from public.ventas_re;"
                    cur.execute(sql)
                    resultados = cur.fetchall()
                    message = "000" + str(10) + "_vt__"
                    for resultado in resultados:
                        r1 = str(resultado[0])
                        message = message + r1 + ","
                        r1 = str(resultado[1])
                        message = message + r1 + ","
                        r1 = str(resultado[2])
                        message = message + r1 + ","
                        r1 = str(resultado[3])
                        message = message + r1 + ","
                        r1 = str(resultado[4])
                        message = message + r1 + ","
                        r1 = str(resultado[5])
                        message = message + r1 + ","
                        r1 = str(resultado[6])
                        message = message + r1 + ","
                        r1 = str(resultado[7])
                        message = message + r1 + ","
                        r1 = str(resultado[8])
                        message = message + r1 + "|"
                else:
                    message = "00010sinit_vt__"
                #message= input(" -> ")

        mySocket.close()

if __name__ == '__main__':
    Main()

#Cuando es llamado el servicio, descompone la data para dejar solo el contenido importante
#El servicio recibe un hola mas un numero, luego le suma uno a ese numero y responde
