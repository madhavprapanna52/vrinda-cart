'''
Executor
    Mentain a queue for the central task management
        - ALl backend calls can hit for request
        - with order execution part
'''
from queue import Queue
import sqlite3 as sql
from dataclasses import dataclass
from typing import Tuple, Any

# Data module
@dataclass
class Task:
    table: str
    columns: Tuple[str, ...]
    values: Tuple[Any, ...] # Handeling int and string
    
key_list = "name,price,stock".split(",")
val_list = "rool,10,10".split(",")

def build_insert(table: str, columns: tuple):
    cols = ", ".join(columns)  # Makes joined items
    placeholders = ", ".join(["?"] * len(columns)) # perfect placeholder safe
    return f"insert into {table} ({cols}) values ({placeholders})"

key = tuple(key_list)
val = tuple(val_list)


t1 = Task(
    table="products",
    columns=key,
    values=val
)

print(f"Task is as such {t1}")


class Executor:
    """
        Central Execution unit
     making ordered execution system for all dataflow
    """
    def __init__(self, connection_file):
        self.connection_file = connection_file
        self.order = Queue(maxsize=10)

    def add(self, task):
        self.order.put(task)

    def run(self):
        connection = sql.connect(self.connection_file)
        cursor = connection.cursor()

        while True:
            task = self.order.get()
            try:
                query = build_insert(task.table, task.columns)
                print(f"final query for execution {query}")
                cursor.execute(query, task.values)
                connection.commit()
                print(f"Executed : {task.values} with {query}")
            except Exception as e:
                connection.rollback()
                print(f"Query faild with {e}")
            finally:
                self.order.task_done()
connection_file = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"
h = Executor(connection_file)
h.add(t1)
h.run()

val = "lamp,10,10".split(".")
val = tuple(val)

t2 = Task(
    table="products",
    columns=key,
    values=val
)

h.add(t2)




h.add(t2)
