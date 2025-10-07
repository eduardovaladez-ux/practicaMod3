import psycopg2

#Conexión a la base de datos
conexion = psycopg2.connect(
    host = "localhost",
    port = "5432", #Es el puerto que escucha postgress
    database = "credenciales",
    user = "Admin",
    password = "p4ssw0rdDB"
)

#Crear cursor
cursor = conexion.cursor()

#Ejecutar consulta
cursor.execute("SELECT * FROM usuarios")
#fetchone() = una fila
#fetchmany(n) = hasta n filas
registros = cursor.fetchall() #Recuperar todas las filas devueltas
#Registros almacena en tuplas

for fila in registros:
    print(fila)

#Cerrar la conexión
cursor.close()
conexion.close