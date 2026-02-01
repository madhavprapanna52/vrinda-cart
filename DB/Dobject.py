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
import time


@dataclass
class Task:
    query:str
    data: Tuple[Any, ...]
    status : str = "pending"  # pending | done | failed


class Dobject:  # working 
    def __init__(self, handle, table_name, columns_list, anchor):
        '''
        Data information
        information => key:value
        handles => {executor:handle, fetch:handle}

        Initiation flow
        search DB --> Initiate if exist --> terminate initiation
        '''
        self.anchor = anchor  # identification of Element
        self.information = {}  # sync updates information dictioinary
        self.columns_list = columns_list
        self.table_name = table_name

        # Handles and connections
        path = os.getenv("DB_LINK")
        self.fetch = Fetch()
        self.executor = handle
        self.query_builder = QueryBuilder(self.table_name)

    def sync(self):  # working 
        ''' Makes DB-Synced information dictionary
        Make request to DB with anchor information
        iterate and update the information dictionary 
        returns : bool [ check for existence and initiation status ]
        '''
        
        condition_string, value = self.anchor # tuple -> info 
        value = tuple([value])
        query = self.query_builder.instance(condition_string=condition_string)

        status, result = self.fetch.filter(query,value)

        print(f"Result fetch for sync : {result}")
        if status:
            for k, v in zip(self.columns_list, result[0]):
                self.information[k] = v  # Information update
            print(f"SYNC RESULT : {self.information}")
            return True # success with sync
        else:
            return False

    def fetch_information(self, required_column):  # working
        ''' Makes fetch request and takes required column from target '''
        self.sync()
        r = self.information[required_column]
        print(f"See After sync , {r}")
        return r  # returns the required information 

    def create(self, information):
        '''
        creation request flow
        information dictionary --> validates with columns list
        make creation request + update anchor information
        request for creation --> commit for creation and edit anchor information
        sync with DB

        Information
        ~ No validation used for information dictionary Back-end handel with frontend request
        '''
        columns = list(information.keys())

        # Making payload for creation
        creation_query = self.query_builder.create(columns)
        values = tuple(list(information.values()))
        # creating task object
        creation_task = Task(
            query=creation_query,
            data=values
        )

        # requesting Executor
        self.executor.tasks.put(creation_task)
        # FIX : time.sleep(1)  # without time constraints the main fails
        # Inspecting task timeline
        print(f"Task status just after joining the queue : {creation_task.status}")
        time.sleep(2)
        print(f"Task status after one second {creation_task.status}")
        
        # Updating Anchor information
        self.anchor = (columns[0], values[0])  # taking id pair as anchor
        print(f"Updated Anchor information for sync to work with : {self.anchor}")
        self.sync()  # sync function for Object-DB sync New initialised


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
        self.executor.tasks.put(task)
        self.sync()


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

