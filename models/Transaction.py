"""
    Mini transaction DB connection unit for storing user history

"""
from config import *


def transaction_db(final_bill, user_id, db_endpoint):
    db_endpoint = db_endpoint
    final_dict = {
        "customer_id" : user_id,
        "product_id" : 0,
        "stock" : 0
    }
    for elem in final_bill:
        print(f"elemenet is {elem} with type : {type(elem)}")
        product_id = elem[0]
        stock = elem[1]
        final_dict["product_id"] = product_id
        final_dict["stock"] = stock
        print(f"Final dictionary : {final_dict}")
        db_endpoint.create_row(final_dict)
        log.info("Check out transaction db for update regards the purchase")
