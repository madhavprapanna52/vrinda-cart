"""
Central Executor
Loads query and executes into DB
"""
from queue import Queue
import sqlite3 as sql
from dataclasses import dataclass
from typing import Tuple, Any

# Fundamental Data models for operation
@dataclass
class Create:
    ''' Creating new object '''
    table: str
    columns: Tuple[str, ...]
    values: Tuple[Any, ...]

@dataclass
class Edit:
    ''' Task for Editing given anchored dataset '''
    table: str
    edit_column: str
    edit_value: str
    anchor_info: Tuple[Any, ...]


def build_insertion(columns, table_name):
    places = ", ".join(columns)
    placeholder = ", ".join(["?"] * len(columns))
    query = f"INSERT INTO {table_name} ({places}) VALUES ({placeholder})"
    return query

def add_condition(value):
    if type(value) == str:
        return f"'{value}'"
    else:
        return str(value)

def build_edit( edit_colum, anchor_info, table_name):
    '''
        Load the edit info value at execute function due to complexity of data breaches
    '''
    value = anchor_info[1]
    query = f"UPDATE {table_name} SET {edit_colum} = ? WHERE {anchor_info[0]} = "
    query += add_condition(value)
    return query  # needs to add the edit information at loading it into DB

def build_destroy(anchor_info, table_name):
    value = anchor_info[1]
    query = f"DELETE FROM {table_name} WHERE {anchor_info[0]} = "
    query += add_condition(value)
    return query

def query_builder(task):
    ''' input : task 
        ouptut : query \ querry with insertion data tuple
    '''
    if type(task) == Create:
        columns = task.columns
        values = task.values
        table_name = task.table

        query = build_insertion(columns, table_name)
        return query, values
    elif type(task) == Edit:
        query = build_edit(task.edit_column, task.anchor_info, task.table)
        print(f"query for edit : {query}")
        value = []
        value_elem = task.edit_value
        value.append(value_elem)

        value = tuple(value)
        print(f"Edit final retuns query as : {query} and data as : {value}")
        return query, value
    
    else:
        print("Working ...")


class Executor:
    def __init__(self, path):
        self.path = path
        self.order = Queue(maxsize=10)

    def add(self, task):
        self.order.put(task)

    def run(self):
        connection = sql.connect(self.path)
        cursor = connection.cursor()

        while True:
            task = self.order.get()
            try:
                query, data = query_builder(task)
                cursor.execute(query, data) # Should work for Making final edits into DB
                connection.commit()
                print(f"working DB write done :)")
            except Exception as e:
                connection.rollback()
                print(f"Something wrong engeninear here :) {e} ")

class Search:
    """
        Central Search unit for searching DB information
    fetch usefull information via independent connections for each fetch request
    """
