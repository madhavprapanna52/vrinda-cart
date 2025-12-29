"""
    Generalised Back-end end point for DB connection
    Features
    Makes an generalised end point for objects to make Db transactions
        - update
        - fetch 
        - delete
"""
import sqlite3

connection = sqlite3.connect("vrinda-cart.db")
cursor = connection.cursor()

# DB  Execution function
def execute_it(querry, output_required):
    if output_required:
        print(f"fExecution thing with {querry}") # Whats that grey thing ?? check out that : )
        cursor.execute(querry)
        output_list = cursor.fetchall() # for fetching instance or DB debug
        return output_list
    cursor.execute(querry)
    connection.commit()
    print(f"[*] Querry Executed with request {querry}")

# TODO testing required for DB object
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

    def create_row(self, data):
        """
            data : dictionary of key value pair
        """
        querry = f"insert into {self.table_name}"
        values = tuple(data.keys())  # values 0th element should be unique
        data = tuple(data.values())
        querry += f" {values} " + f" {data} "
        output = execute_it(querry, 1)
        print(f"Row creation output : {output}")
        specific = ("id", )
        id = self.search_row("id",["name",values[0]])
        print("creation success full")
        return id




    def edit_column(self, column_name, data, target_id):
        if type(data) is str:
            querry = f"update {self.table_name} set {column_name} = '{data}' where id = {target_id}"
            execute_it(querry) # Querry executed
        else:
            querry = f"update {self.table_name} set {column_name} = {int(data)} where id = {target_id}"
            execute_it(querry)  # Executed querry
        print(f"[*] Debug required with data : {data} and {column_name} collumn")

    def delete_column(self, target_id):
        querry = f"delete from {self.column_name} where id = {target_id}"
        execute_it(querry)
        print("Delete Querry Executed")

    def search_row(self, target, value):
        '''
            If specific is given for string target then we can fetch
        '''
        print(f"Initiating with {target} and {value}")
        if type(target) is str:
            querry = f"select {target} from {self.table_name} where {target} = '{value}'"

            print(f"Querry for injecting : {querry}")
            output = execute_it(querry,1)
            return output

        # compose querry with required values
        querry = f"select *  from {self.column_name} where id = {target}"
        result = execute_it(querry, 1) # expected to fetch output
        return result # Exepcted to fetch required output or refine with instance search

    def fetch_instance(self):
        querry = f"select * from {self.table_name}"
        output_list = execute_it(querry, 1)
        for i in output_list:
            print(i) # Improvement | Make it into string to fetch important things like colum informations


