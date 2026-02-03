from DB.QueryBuilder import *
from DB.Execute import executor


# Working Object Unit
class Object:
    def __init__(self, table):
        self.table = table
        self.query = QueryBuilder(self.table)

    def create(self, information: dict):
        columns = list(information.keys())
        values = tuple(information.values())

        query = self.query.create(columns)
        return executor(query, values)

    def fetch(self, columns="*", anchor=None):
        """
        anchor = ("id", 5) or None
        """
        if anchor:
            query = self.query.instance(columns, anchor[0])
            return executor(query, (anchor[1],), fetch=True)
        else:
            query = self.query.instance(columns)
            return executor(query, fetch=True)

    def edit(self, anchor, edit_information):
        """
        anchor = ("id", 5)
        edit_information = ("price", 199)
        """
        query = self.query.edit(edit_information[0], anchor[0])
        values = (edit_information[1], anchor[1])
        return executor(query, values)

    def delete(self, anchor):
        """
        anchor = ("id", 5)
        """
        query = self.query.delete(anchor[0])
        return executor(query, (anchor[1],))

