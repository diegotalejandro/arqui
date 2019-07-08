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
        message = "00010sinit_dv__"

        while message != 'q':
                #print (message)
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                #print ('Received from server: ' + data)
                data2 = "".join(data)
                if data2[5:10] == "_dv__":

                    number = int(data2[0:5])
                    respuesta = data2[10:number+5]
                    respuestas = respuesta.split(",")

                    sql = "select * from public.menu where id=" + str(respuestas[4]) + ";"
                    cur.execute(sql)
                    result = cur.fetchall()
                    print (result)
                    if result!=[]:
                        numero = str(random.randrange(10,1000))
                        sql = "insert into public.delivery values (" + numero
                        sql = sql + ", '" + str(respuestas[0])
                        sql = sql + "', '" + str(respuestas[1])
                        sql = sql + "', '" + str(respuestas[2])
                        sql = sql + "', '" + str(respuestas[3])
                        sql = sql + "', '" + str(result[0][1])
                        sql = sql + "', " + str(result[0][0])
                        sql = sql + ", " + str(5000)
                        sql = sql + ", '2019-07-08', '" + str(respuestas[5])
                        sql = sql + "', '" + str(respuestas[6])
                        sql = sql + "');"
                        print (sql)
                        cur.execute(sql)
                        conn.commit()
                        message = "000" + str(10) + "_dv__" + "OK"
                    else:
                        message = "000" + str(10) + "_dv__" + "NK"
                    #resultados = cur.fetchall()

                else:
                    message = "00010sinit_dv__"
                #message= input(" -> ")

        mySocket.close()

if __name__ == '__main__':
    Main()

#Cuando es llamado el servicio, descompone la data para dejar solo el contenido importante
#El servicio recibe un hola mas un numero, luego le suma uno a ese numero y responde
