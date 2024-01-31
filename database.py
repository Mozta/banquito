import psycopg2

# db = 'banquito'
user = 'admin'
password = 'admin'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(f"user={user} password={password} host={host} port={port}")
cur = conn.cursor()

cur.execute("create DATABASE banquito")
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS cuentas (
#         id SERIAL PRIMARY KEY,
#         saldo DECIMAL(10, 2) NOT NULL
#     )
# """)

cur.commit()
cur.close()
conn.close()