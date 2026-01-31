import threading
from DB.ExecutorHandle import *
from models.Productv1 import *
from DB.Dobject import *


handle = Executor()

threading.Thread(
    target=handle.run,
    daemon=True
).start()


info = ("name", "mac")

db_handle = Dobject(handle, "products")
'''
Initiation of Models
 + Search for existing product with anchor information
 + Fetch and sync with DB
 + Make edits and sync with DB-about information of the object
'''
p = Product(info, db_handle)
print(f"Product Initiated with information : {p.information}")
p.stock()  # NEEDs to check with sync function for validating request

print(f"Product after stock update : {p.information}")
