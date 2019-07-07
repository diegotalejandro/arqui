import psycopg2

#host = "local socket"
#port = 5432
#user = ""
#passwd=""
#database = "postgres"

conn = psycopg2.connect("dbname=postgres")
cur = conn.cursor()


def Main():
    	sql = "select * from public.asistencia;"
    	cur.execute(sql)
    	resultados = cur.fetchall()
    	r1= resultados[0]
    	print (r1)

if __name__ == '__main__':
    Main()

#Cuando es llamado el servicio, descompone la data para dejar solo el contenido importante
#El servicio recibe un hola mas un numero, luego le suma uno a ese numero y responde
