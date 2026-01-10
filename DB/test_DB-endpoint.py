from General_Object import *
from Endpoint import *

endpoint = Endpoint("products")

information = {"name":"mac-book", "prize":150,"stock":10}

feilds = 'id,name,prize,stock'.split(',')
product = General_Object(information, feilds, endpoint)
print(f"Product information {product.information}")
edit_list = ("name","mac-book-pro-max-ultra")

product.update(edit_list)
print(f"Product updated with new information : {product.information}")


