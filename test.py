import threading
from DB.Execute import *
from DB.DB_Endpoint import *

path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"
central_executor = Executor(path)

threading.Thread(
    target=central_executor.run,
    daemon=True
).start()

product_endpoint = Endpoint("products", central_executor)

product_endpoint.search()
