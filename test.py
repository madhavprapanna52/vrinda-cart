from DB.Object import *

product = Object("products")

anchor = ("id",1)
edit_info = ("name", "Accer-Alg-gaming")
e = product.edit(anchor, edit_info)
print(f"output :e {e}")
