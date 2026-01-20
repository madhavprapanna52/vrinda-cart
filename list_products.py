from models.Product import *
from DB.Endpoint import *

pr = Endpoint('products')
products = [{"name" : "Mac-book", "prize" : 100000, "stock" : 10}, {"name" : "Rolls-Royce", "prize" : 1000000, "stock":10}]
for p in products:
    Product(p, pr)


