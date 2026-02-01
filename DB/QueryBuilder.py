"""
    Generates Query for requirements and dataset
Building query

Head : Target table information -> Requested dataset -> conditions if required
    + target and required data -> Via f string [ Back-end calls validation required]
    + adding conditions via placeholder information 

    creation request specific ~ placeholder mechanism required

Query 
    1. create
        req : columns | placeholder for placing values for creation
    2. edit
        req: targeted colum to edit, conditions | placeholder for which to thing to add
    3. delete
        req: condition | no placeholder 
"""

class QueryBuilder:
    '''
    target centric and builds query for required table and responds with query string
    '''
    def __init__(self, table_name):
        self.table = table_name

    def create(self, columns):
        column_string = ", ".join(columns)
        placeholder = ", ".join(["?"] * len(columns))

        query = f"insert into {self.table} ({column_string}) values ({placeholder})"
        return query
    
    def edit(self, target_column:str, condition_information:str):
        column = condition_information
        query = f'update {self.table} set {target_column} = ? where {column} = ?'
        return query

    def delete(self, condition_column:str):
        query = f"delete from {self.table} where {condition_column} = ?"
        return query  # requires the condition value at execution
    
    def instance(self, required_columns="*", condition_string=""):

        if type(required_columns) == list:
            required_columns = ", ".join(required_columns)
        query = f"select {required_columns} from {self.table}"
        # if condition is given we would fetch target information
        if len(condition_string) > 1:
            query += f" where {condition_string} = ?"
            return query
        else:
            return query



