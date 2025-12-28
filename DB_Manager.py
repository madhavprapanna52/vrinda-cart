"""
    function : Managing data base peristency and doing core crude operations

    Features
        - Adding Objects to the db
        - Removing objects
        - Finalizing crude operations
"""

import sqlite3

conn = sqlite3.connect("vrinda-cart.db")
cursor = conn.cursor()


def init_product(product_data):  #  tested ok
    """
    returns :: Product Id of creation for references 
    Usage : products db is controlled by products themself , they control their name and prize
    PRODUCT MANAGER would do changes via product utilities and manage stock with different units
        input : tuple based data (id, productname, product prize 
        output : Making DB ENtries and loging state changes
    """
    querry = """
        INSERT INTO products (name, prize, stock) VALUES (?, ?, ?);
    """
    # Product_data -> Consisting of product name, prize
    print("Used product_data", product_data)
    cursor.execute(querry,product_data)
    conn.commit()
    print(f"Inserted Product data into DB : {product_data}")
    print(cursor.execute("SELECT * from products").fetchall())

def fetch_db():
    cursor.execute("SELECT * from products")
    fetched = cursor.fetchall()
    for row in fetched:
        print(row) # fetched information

def fetch_target(id):
    print(f"got id as {id}")
    f = f"select name, prize from products where id = {id}" #TODO Fix error with id and data flow
    print(f"querry set : {f}")
    cursor.execute(f"select name from products where id = {id}")
    row = cursor.fetchall()
    print(f"Row dataset : {row}")

def update_db(opt, data, id): # tested ok
    """
        Input : operation : 1 : name update , 2: prize update
        return updates the data base state
"""
    # ISSUE Single sql querry cant generalised for different data types as we have prize and name
    global row_target
    if opt == 1:
        q = f"update products set name = '{data}' where id = {id}"
    elif opt == 2:
        q = f"update products set prize = {data} where id = {id}"

    # TODO optimize querry building part and iterations
    print(f"Querry being loaded for execution : {q}")
    cursor.execute(q)
    conn.commit()

def delete(id):  # tested ok | Data base clashes 
    print(f"Id being provided {id}")
    q = f"delete from products where id = {id}"
    cursor.execute(q)

    conn.commit()

