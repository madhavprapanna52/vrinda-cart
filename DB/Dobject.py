"""
    Dobject
Data base object data flow unit
+ elemental data flow management
+ sync with object 
+ Initiation only if exist
+ create tool for creating the required data entry first
"""
from DB.FetchHandle import *
from DB.QueryBuilder import *
import os
from typing import Tuple, Any
from dataclasses import dataclass


@dataclass
class Task:
    query:str
    data: Tuple[Any, ...]
    status : str = "pending"  # pending | done | failed

    # TODO : Make fetching function at Dobject for reading informations about a target
class Dobject:
    def __init__(self, handle, table_name):
        '''
        Data information
        information => key:value
        handles => {executor:handle, fetch:handle}

        Initiation flow
        search DB --> Initiate if exist --> terminate initiation
        '''
        path = os.getenv("DB_LINK")
        print(f"Path fethced with env : {path}")
        self.fetch = Fetch()
        self.executor = handle

        self.table_name = table_name
        self.build_query = QueryBuilder(self.table_name)


    def exist(self, information):
        ''' information ~ (column, value) '''
        anchor = information[0]
        value = information[1]
        # tuple data due to executor constraints
        data = [value]
        data = tuple(data) 

        query = self.build_query.instance(condition_string=anchor)
        result = self.fetch.filter(query, data)

        if result:
            return True, result
        else:
            return False,[]

    def create(self, information):
        anchor = list(information.keys())[0]
        value = information[anchor]
        
        info = [anchor, value]
        result = self.exist(info)
        if result[0]:
            return False # Existence Based termination
        columns = list(information.keys())
        values = tuple(list(information.values()))
        creation_query = self.build_query.create(columns)
        print(f"Creation Query : {creation_query}")
        
        task = Task(
            query=creation_query,
            data=values
        )
        print(f"Task Made as {task}")
        print(f"Run next time with including thread for execution function")
        self.executor.tasks.put(task)
        self.executor.run()  # Making query to run :)
        return task.status

    def edit(self, edit_information, anchor_information):
        '''
        edit_information : (column_to_edit, final_thing )
        Information dict -> anchor information
        build query for edit(anchor information, edit_information)
        make execution request for edits

        Flow
        edit information -> build query -> execution request
        '''
        target_column = edit_information[0]
        condition_information = anchor_information[0]
        query = self.build_query.edit(target_column, condition_information)
        values = [edit_information[1], anchor_information[1]]
        values = tuple(values) # values information
        # Edit task information
        task = Task(
            query=query,
            data=values
        )
        print(f"final Task for making edit : {task}")
        self.executor.tasks.put(task)
        return task.status

    def delete(self, anchor_information):
        # INFO : No cascade operation happens after delete query 
        s = anchor_information[0]
        query = self.build_query.delete(s)

        values = [anchor_information[1]]
        values = tuple(values)

        task = Task(
            query=query,
            data=values
        )

        self.executor.tasks.put(task, values)
        return task.status

