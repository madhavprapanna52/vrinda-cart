"""
Main application interface
    Implementing distributed blueprint based routing system
    Handle core logic via using tools for making authentication and routing features
"""
from flask import Flask, render_template
from products_page import products_page
from login_route import login_page

app = Flask(__name__)
app.register_blueprint(products_page, url_prefix='/products')
app.register_blueprint(login_page, url_prefix="/login")


@app.route("/")
def landing_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
