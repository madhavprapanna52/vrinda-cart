"""
Executor
Central Execution flow for all DB requests
Taking taks and Doing them to deliver results
"""
from queue import Queue
import sqlite3 as sql
from dataclasses import dataclass
from typing import Tuple, Any
#import config

# Task Data Model
'''
    Used for Objectified task model which would be used for making task
    and using their dataflow to execute and log information
'''

@dataclass
class Task:
    query_type: str
    table: str
    columns: Tuple[str, ...]
    values: Tuple[Any, ...]  # INFO : serialise muAltiple data vrinda-carta external loops
    anchor: list[Any, ...]


def build_query(task):
    '''
        Makes simple query for Execution
    q_type list to evaluate and feature
    insertion query : i
    update query : u
    delete : d

    INFO : Load loops for mass execution and these would handle row based insertions for now :)
    '''
    cols = ", ".join(task.columns)  # Columns string
    placeholders = ", ".join(["?"] * len(task.columns)) # placeholder string
    query = ""  # default and error results blank
    if task.query_type == "i": 
        query = f"INSERT INTO {task.table} ({cols}) VALUES ({placeholders})"
    if task.query_type == "u":  # FIX : requires  validated pipeline for execution system :)
        if len(anchor) == 0:
            print(f"Terminating Edit request anchor not given :) ")
            return None
        anchor_col = taask.anchor[0]
        anchor_val = task.anchor[1]
        query = f"UPDATE {table} SET ({cols}) = ({placeholders}) WHERE {anchor_col} = {anchor_val}"  # FIX : Anchor and where is broken again :)
    return query  # Expand for other options


class Executor:
    '''
        Central Query Executing system
    inputs : query_type, task
    output : None if operative query or results if fetch query initiated
    '''
    def __init__(self, path):
        self.connection_file = path
        self.order = Queue(maxsize=10) # Limmiting test

    def add(self, task):
        print("task added to run")
        self.order.put(task)

    def run(self):
        print(f"Running executor run function :)")
        connection = sql.connect(self.connection_file)
        cursor = connection.cursor()

        while True:
            task = self.order.get() # Taking task from queue
            try:
                query = build_query(task)
                #log.info(f"Final Query for DB call : {query}")
                cursor.execute(query, task.values)
                connection.commit()

            except Exception as e:
                connection.rollback()
                #log.warning(f" [Failed] Exector failed with Error : {e}")
            finally:
                self.order.task_done()
