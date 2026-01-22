"""
Features
    1. Route handeling
    2. Data flow and main communication flow
"""
from models.Product import *
from DB.Endpoint import *
from flask import Blueprint, render_template,request

product_endpoint = Endpoint("products")
product_list = product_endpoint.fetch_instance("name,prize") # INFO : Not the best way to fetch db :)

products_page = Blueprint('products',__name__)

print(f"Product list : {product_list}")

# TODO : Make working user login and product listing feature | wrap project complete

@products_page.route('/', methods=['GET'])
def products():
    if request.method == "GET":
        return render_template("products.html", product_list=product_list)
