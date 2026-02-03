import os
import sqlite3 as sql

path = os.getenv("DB_LINK")

def executor(query, data=None, fetch=False):
    with sql.connect(path) as connection:
        connection.execute("PRAGMA foreign_keys = ON;")
        cursor = connection.cursor()
        try:
            if data is not None:
                cursor.execute(query, data)
            else:
                cursor.execute(query)

            if fetch:
                return cursor.fetchall()

            connection.commit()
            return 1  # success
        except Exception as e:
            print(f"DB Exception: {e}")
            return 0

