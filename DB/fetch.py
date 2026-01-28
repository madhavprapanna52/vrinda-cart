'''
    Central DB truth fetching unit
Handeling all fetch requests for giving the required data state at given time
'''
import sqlite3 as sql

def search(table, targets, anchor_dict, connection):
    cols = ", ".join(anchor_dict.keys())
    placeholder = ", ".join(["?"] * len(anchor_dict.keys()))

    targets = ", ".join(targets)

    vals = tuple(anchor_dict.values())

    query = f"SELECT {targets} from {table} where ({cols}) = ({placeholder})"
    print(f"search query made out as : {query}")
    fetch_handle = connection.cursor()

    try:
        fetch_handle.execute(query, vals)
        result = fetch_handle.fetchall()
        return result
    except Exception as e:
        print(f"Exception occured while fetching as {e}")
        return None

path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"
connection = sql.connect(path)

d = {"name" : "GigaBite"}
target = ["stock", "price", "id"]
output = search("products", target, d, connection)
print(f"Fetch results as {output}")

