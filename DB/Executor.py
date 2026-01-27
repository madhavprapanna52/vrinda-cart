'''
    Executor
Single unit for handeling all SQL Operations , making operations via FILO based system
Handeling all query and being into single thread for execution of query

'''

class Executor:
    def __init__(self):
        self.connection = "connection_file"
        self.cusor = self.connection.cursor()
        self.execution_list = []

    def add(self, query, data=""):
        element = {}
        element["query"] = query
        element["data"] = data
        self.execution_list.append(element)  # query list

    def perform(self, fetch=False):
        print(f"Executor Running for tasks {self.execution_list}")
        for element in self.execution_list:
            q = element["query"]
            d = element["data"]  # shape : tuple 
            try:
                self.cursor.execute(q, (d,))
                if fetch:
                    return self.cursor.fetchall()  # return type list of tuple
            except Exception as e:
                print(f"Something went wrong as {Exception}")
                return 0
