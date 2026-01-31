import threading
from DB.ExecutorHandle import *
from models.Productv1 import *
from DB.Dobject import *


handle = Executor()

threading.Thread(
    target=handle.run,
    daemon=False
).start()


info = {
    "name" : "Accer-Lapatopa",
    "price" : 10,
    "stock" : 10
}

db_handle = Dobject(handle, "products")

p = Product(info, db_handle)
p.stock()
