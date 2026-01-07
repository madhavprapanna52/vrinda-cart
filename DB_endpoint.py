"""
    Generalised Back-end end point for DB connection
    Features
    Makes an generalised end point for objects to make Db transactions
        - update
        - fetch 
        - delete
"""
import sqlite3
import logging as log

# Loging config
log.basicConfig(
    filename="app.log",      # file name
    level=log.INFO,       # minimum level to record
    format="%(asctime)s | %(levelname)s | %(message)s"
)


connection = sqlite3.connect("vrinda-cart.db")
cursor = connection.cursor()

# DB  Execution function
def execute_it(querry, output_required=0):
    if output_required == 1:
        cursor.execute(querry)
        output_list = cursor.fetchall() # for fetching instance or DB debug
        return output_list
    else:
        cursor.execute(querry)
        connection.commit()

# TODO testing require for modification operations , creation working
class DB_object:
    """
        Makes db connection for the object to perform basic operations 
        working
            > Connects to DB for making requests for object
            > Ensures DB operations work
        Procedue 
            ~ Build Querry string for operations with respect to the table name

    Responsible for
        - editing
        - deleting
        - viewing
        - creating non existig object
    """
    def __init__(self, table_name):
        self.table_name = table_name  # core table name
        self.instance = self.fetch_instance() # Fetch current state of DB
        # check instance for existance

    def create_row(self, data):  # tested ok Working
        """
            data : dictionary of key value pair
        """
        querry = f"insert into {self.table_name}"
        values = tuple(data.keys())  # values 0th element should be unique
        data = tuple(data.values())
        # Querry is to the made with strict format
        querry += f" {values} " + f"values {data} "
        log.info(f"Injecting creation statement as : {querry}")
        cursor.execute(querry)
        connection.commit()
        output = self.fetch_instance()  # Instance after creation
        log.info(f"Row creation output recieved :: \n {output} \n")
        if output:
            return 1
        else:
            log.fatal("Not created for data request")
            return 0



    def edit_column(self, column_name, data, target_id): # under testing
        if type(data) is str:
            querry = f"update {self.table_name} set {column_name} = '{data}' where id = {target_id}"
            log.info(f"Update Querry requested to DB : {querry}")
            execute_it(querry) # Querry executed
        else:
            querry = f"update {self.table_name} set {column_name} = {int(data)} where id = {target_id}"
            log.info(f"Update Querry requested to DB : {querry}")
            execute_it(querry)  # Executed querry

    def delete_column(self, target_id):
        querry = f"delete from {self.column_name} where id = {target_id}"
        execute_it(querry)
        log.info(f"Deleted ROW with id : {target_id}")

    def search_row(self, target, value=""):  # Tested OK 
        '''
            If specific is given for string target then we can fetch
        '''
        log.info(f"Searching for existing Product with collum : {target} and value :{value}")
        if type(target) is str:
            querry = f"select * from {self.table_name} where {target} = '{value}'"

            log.info(f"Searching querry \n : {querry} \n")
            output = execute_it(querry,1)

            log.info(f"Search result Target fetched : \n {output} \n")

            return output

        # CRITICAL No screening for target is placed here
        querry = f"select *  from {self.table_name} where id = {target}"
        result = execute_it(querry, 1) # expected to fetch output
        log.info(f"ID searched |  id : {target} results : {result}")
        return result # Exepcted to fetch required output or refine with instance search

    def fetch_instance(self):  # tested OK 
        querry = f"select * from {self.table_name}"
        cursor.execute(querry)
        output = cursor.fetchall()

        db_instance = "{{ DB-Instance fetched }} \n"

        for row in output:
            db_instance += f"{row} \n"
        return db_instance


# Generalised Object

class General_obj:
    '''
        Base entity for all objects
        Initiate DB-endpoint at big level for consistency
        endpoint = DB_endpoint for respected table

        Usage options
        Mentain data details in dictonary as per schema
        request for edits in list of tuples for edits
        flows data in dictionary for edits

    '''
    def __init__(self,obj_details, end_point, search_anchor=""):
        """
            Search anchor based searching could be used for id based initialization
        """
        self.end_point = end_point
        self.obj_information = {}

        # search fetch anchor details are assumed as second data details
        feilds = list(obj_details.keys())  # take feild list would be taken as argument
        if search_anchor == "":
            search_anchor = feilds[0]
            anchor_value = obj_details[search_anchor]
        else:
            anchor_value = obj_details[search_anchor]  # searching word

        # Dual Initiation logicanchor_value)

        db_fetch = self.end_point.search_row(search_anchor,anchor_value)
        if db_fetch == []:
            log.warning(f"Searched for {anchor_value} Failed | Creating one Entry")
            self.end_point.create_row(obj_details)
            db_fetch = self.end_point.search_row(search_anchor, anchor_value)
            
        data_tuple = db_fetch[0] # DB response
        i = 0
        self.obj_information["id"] = data_tuple[0]  # Id required
        for d in data_tuple[1:]:
            self.obj_information[feilds[i]] = str(d)
            i += 1

    def info(self):
        print(f"Object information fetched : {self.obj_information}")

    def update(self, edit_list):
        for edit in edit_list:
            target_colum = edit[0]
            data = edit[1]
            self.end_point.edit_column(target_colum, data, int(self.obj_information["id"]))
            log.info("Edits Executed")
            log.info(f'Inspect changes : \n {self.end_point.fetch_instance()} \n ')

