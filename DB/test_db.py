from Dobject import *
from ExecutorHandle import *


information = {"name":"Accer-laptop", "price":10, "stock":10}
handle = Executor()
table_name = "products"
path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"




d = Dobject(handle, table_name)

edit_information = ["name", "Mercedees"]
anchor_information = ["id", 1]  # test with one as string

r = d.edit(edit_information, anchor_information)  # End point request
print(f"creation result as : {r}")
