# Biblioteca 
import mysql.connector 


# Programa
print ("Conectandose a la base de datos")
cnx = mysql.connector.connect(user='Alejoel', password='ale100901',
                              host='127.0.0.1',
                              database='codigoIoT')
print ("Conexión exitosa")
print(cnx)

print ("Cerrando conexion")
cnx.close()
print ("Conexion cerrada")
