import psycopg2

# db = 'banquito'
# user = 'postgres'
# password = '1234'
# host = 'localhost'
# port = '5432'

# conn = psycopg2.connect(f"user={user} password={password} host={host} port={port} dbname={db}")
# cur = conn.cursor()

# cur.execute("""
#     CREATE TABLE IF NOT EXISTS cuentas (
#         id SERIAL PRIMARY KEY,
#         saldo DECIMAL(10, 2) NOT NULL
#     )
# """)

# # cur.execute("INSERT INTO cuentas (saldo) VALUES(%s)", (500.0,) )
# cur.execute("SELECT * FROM cuentas")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# conn.commit()
# cur.close()


class DB:
    def __init__(self):
        db = 'banquito'
        user = 'postgres'
        password = '1234'
        host = 'localhost'
        port = '5432'
        print("Inicializando database...")
        self.conn = psycopg2.connect(f"user={user} password={password} host={host} port={port} dbname={db}")
        self.cur = self.conn.cursor()

    def mostrar_cuentas(self):
        self.cur.execute("SELECT * FROM cuentas")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.conn.commit()

    def obtener_cuentas(self):
        self.cur.execute("SELECT * FROM cuentas")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.conn.commit()
        return rows

    def crear_cuenta(self):
        try:
            self.cur.execute("INSERT INTO cuentas (saldo) VALUES(%s)", (0.0,) )
            self.conn.commit()
            return True
        except:
            return False

    def actualizad_saldo(self, id, saldo):
        self.cur.execute("UPDATE cuentas SET saldo = %s WHERE id = %s", (saldo, id))
        self.conn.commit()

    def cerrar_db(self):
        self.cur.close()


# db = DB()
# # db.crear_cuenta()
# db.mostrar_cuentas()
# db.actualizad_saldo(2, 100)
# db.mostrar_cuentas()