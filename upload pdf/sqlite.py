import sqlite3


def query():
        conn= sqlite3.connect("DataBase.db")
        cursor = conn.cursor()

        c = cursor.execute(""" SELECT * FROM  tablom """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]

        with open("{}".format(name_v), 'wb') as f:
            f.write(data_v)
        conn.commit()
        cursor.close()
        conn.close()

print()
query()
