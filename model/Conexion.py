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


    def read_cl(self):
        with self.conn.cursor() as cur:
        # Ejecuta y guarda resultados de la primera consulta
            cur.execute('SELECT * FROM "clientes"')
            data2 = cur.fetchall()
        return data2
    
    def read_vt(self):
        with self.conn.cursor() as cur:
            cur.execute('SELECT * FROM "ventas"')
            data3 = cur.fetchall()
        return data3
    
    def read_pr(self):
        with self.conn.cursor() as cur:
            cur.execute('SELECT * FROM "productos"')
            data4 = cur.fetchall()
        return data4


    def write_cl(self, data):
        with self.conn.cursor() as cur:
        # Inserta cliente
            cur.execute("""
            INSERT INTO "clientes" (nombre, correo, telefono)
            VALUES (%(nombre)s, %(correo)s, %(telefono)s)
                """, data)
        self.conn.commit()
            

    def write_vt(self, id_producto, id_cliente):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO ventas (id_cliente, id_producto, fecha)
                VALUES (%s, %s, CURRENT_DATE)
            """, (id_cliente, id_producto))
        self.conn.commit()

    def write_pr(self, data2):
        with self.conn.cursor() as cur:
        # Inserta producto
            cur.execute("""
            INSERT INTO "productos" (nombre, precio)
            VALUES (%(nombre)s, %(precio)s)
             """, data2)
    # Guarda los cambios
        self.conn.commit()

    def delete_cl(self,id_cliente):
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "clientes" WHERE id_cliente = %s
             """, (id_cliente))
        self.conn.commit()

    def delete_vt(self,id_venta):
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "ventas" WHERE id_venta = %s
             """, (id_venta))
        self.conn.commit()

    def delete_pr(self,id_producto):
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "productos" WHERE id_producto = %s
             """, (id_producto))
        self.conn.commit()





    
    def __def__(self):
        self.conn.close()