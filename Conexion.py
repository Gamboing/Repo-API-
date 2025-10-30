import psycopg2

try:
    connection=psycopg2.connect(
        host="localhost",
        user="postgres",
        password="Hadali2203",
        database="guru99"
    )

    print("Conexion exitosa")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM ventas")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

except Exception as ex:
    print(ex)