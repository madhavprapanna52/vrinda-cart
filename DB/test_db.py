from General_Object import *
from Endpoint import *

products_endpoint = Endpoint("products")

info = {
    "name" : "mouse",
    "price" : 2,
    "stock" : 10
}


feilds = "name, price, stock".split(",")
products = General_Object(info, feilds, products_endpoint)


edit = [
    ("name", "mice")
]
#products.update(edit)
