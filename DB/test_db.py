from fetch import *
import sqlite3 as sql
path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"

connection = sql.connect(path)

products_search_handle = Search(connection, "products")

print(f"Instance of product : {products_search_handle.instance()}")

# Target test
targets = "name,id".split(",")
r = products_search_handle.target_cols(targets)
print(f"Result of target_cols : {r}")

a = ("name","GigaBite")
t = products_search_handle.target_search(a)
print(f"Giving target fetch as {t}")

