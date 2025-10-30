import psycopg2
#Conexion a la base de datos postgres usando psycopg2

class UserConnection():
    conn=None

    def __init__(self):
        try:    # Intentar conectar a la base de datos
            self.conn=psycopg2.connect( # Parametros de conexion
                host="localhost",        # Host de la base de datos
                port="5432",             # Puerto de la base de datos   
                user="postgres",         # Usuario de la base de datos
                password="Hadali2203",   # Contraseña del usuario
                database="guru99"        # Nombre de la base de datos
         )

            print("Conexion exitosa")    # Imprime el mensaje de conexion exitosa
            #cursor=self.conn.cursor()   # Crear un cursor para ejecutar consultas
            #cursor.execute("SELECT version()")  # Ejecutar una consulta para obtener la version de la base de datos
            #row=cursor.fetchone()          # Obtener el resultado de la consulta
            #print(row)                  # Imprimir la version de la base de datos
            #cursor.execute("SELECT * FROM ventas") # Ejecutar una consulta para obtener todos los registros de la tabla ventas
            #rows=cursor.fetchall()      # Obtener todos los registros de la consulta
            #for row in rows:        # Iterar sobre los registros y imprimir cada uno 
                #print(row)             # Imprimir el registro

        except Exception as ex:     # Capturar cualquier excepcion que ocurra durante la conexion o la ejecucion de consultas
            print(ex)               # Imprimir el mensaje de la excepcion
            self.conn.close()


    def write(self, data, data1):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "clientes"(nombre, correo, telefono) VALUES(%(nombre)s, %(correo)s, %(telefono)s)
            """, data)
            cur.execute("""
                    INSERT INTO "productos"(nombre, precio) VALUES(%(nombre)s, %(precio)s)
            """, data1)
        self.conn.commit()
    
    def __def__(self):
        self.conn.close()