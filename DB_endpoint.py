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


