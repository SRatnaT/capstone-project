# flake8: noqa

import psycopg2

conn = psycopg2.connect(dbname="capstone_db", user="postgres", password="Arsenal4444!", host="localhost", port="5432")

cur = conn.cursor()

cur.execute("SELECT * FROM api_project")
rows_proj = cur.fetchall()

for row in rows_proj:
    print(row)

cur.execute("SELECT * FROM api_task")
rows_task = cur.fetchall()

for row in rows_task:

    print(row)


cur.close()
conn.close()
