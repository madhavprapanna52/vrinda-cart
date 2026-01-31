from Dobject import *
from ExecutorHandle import *
import threading



information = {"name":"Accer-laptop", "price":10, "stock":10}
handle = Executor()


# Threading Executor for tasks
thread = threading.Thread(
    target=handle.run,
    daemon=False
)

thread.start()



table_name = "products"
path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"




d = Dobject(handle, table_name)

edit_information = ["name", "Rools-royce"]
anchor_information = ["id", 1]  # test with one as string

r = d.delete(anchor_information)  # End point request
print(f"creation result as : {r}")

