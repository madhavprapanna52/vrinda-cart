"""
    Simplified Product Management System

    + List products
    + Manage Products

"""
from DB_Manager import *

product_data = ("Mouse", 100, 11)

init_product(product_data) # Working fine
update_db(2, 5, 1)

# Now list products
fetch_db()
print("deleting function testing")
delete(id)



