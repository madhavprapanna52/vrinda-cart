from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "i am default page "

@app.route('/products')
def show_products():
    return render_template("products_page.html")  # render Products page


if __name__ == '__main__':
    app.run(debug=True)
