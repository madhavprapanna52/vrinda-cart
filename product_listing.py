'''
Product page routing services
1. Making routing for products page
2. Handeling add to cart requst
3. Render template with given information
'''
from flask import blueprint, render_template, request

products_handle = Blueprint("products")
# Ways to rejister for a products page into the blueprint only after authentication workflow

'''
