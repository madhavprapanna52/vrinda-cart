import threading
from DB.Execute import *
from DB.DB_Endpoint import *

path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"
central_executor = Executor(path)

threading.Thread(
    target=central_executor.run,
    daemon=False
).start()

product_endpoint = Endpoint("products", central_executor)

info = {
    "name" : "AccerLaptop",
    "price" : 10,
    "stock" : 10
}

target = ("id" : 1)
product_endpoint.edit(edit, target)


