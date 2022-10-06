# Bibliotecas
import mysql.connector 

# Conexión
cnx = mysql.connector.connect(user='Alejoel', password='ale100901', host='127.0.0.1', database='codigoIoT')
#cursor = cnx.cursor()
print ("Conectado :)")

# Query
query = ("SELECT id, fecha, nombre, temperatura FROM clima WHERE id=16;")

# Ejecucion
# cursor.execute(query)
res = cnx.cmd_query(query)

# Mostrar resultado
print ("Respuesta: ")
print (res)

# Cerrar
#cursor.close()
cnx.close()
print ("Conexion cerrada")