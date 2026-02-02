import threading
from DB.ExecutorHandle import *
from models.Productv1 import *


handle = Executor()

threading.Thread(
    target=handle.run,  # target function starts with thread ad lives even after main thread
    daemon=False
).start()


info = ("name", "mac")  # Anchor information 

new_product = {
    "name" : "Gammer Laptop Nokia",
    "price" : 1700,
    "stock" : 1
}

p = Product(handle, info)

re = p.update_stock()
print(f"Update response {re}")



