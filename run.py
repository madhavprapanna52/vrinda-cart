from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/products')
def show_products():
    return render_template("products_page.html")  # render Products page

@app.route('/login')
def login():
    return render_template("login.html")  # could be used for registration also via jinja

if __name__ == '__main__':
    app.run(debug=True)
