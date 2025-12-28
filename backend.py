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
delete(1)

print("Checking what edits is being done with the data-base")
fetch_db()

print("fetch target testing ***")
print(fetch_target(2)) # Fetch testing
