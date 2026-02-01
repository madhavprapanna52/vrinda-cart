import threading
from DB.ExecutorHandle import *
from models.Productv1 import *
from DB.Dobject import *


handle = Executor()

threading.Thread(
    target=handle.run,
    daemon=False
).start()

# INFO : Threading configurations introduced some inconsistency with the DB-link 


info = ("name", "mac")

new_product = {
    "name" : "Gammer Laptop Nokia",
    "price" : 1700,
    "stock" : 1
}

column_list = "id,name,price,stock".split(",")
db_handle = Dobject(handle, "products",column_list, info)

db_handle.create(new_product)



