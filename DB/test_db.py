from fetch import *
import sqlite3 as sql
from Central_Executor import *


path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"

e = Executor(path)

cols = "name,price,stock".split(",")
vals = ["Rools-Roece",10,10]

cols = tuple(cols)
vals = tuple(vals)
anchor = ["id",1]

anchor = tuple(anchor)

c = Edit(
    table="products",
    edit_column="name",
    edit_value="Mac-OS",
    anchor_info=anchor
)

c2 = Create(
    table="products",
    columns=cols,
    values=vals
)

e.add(c)
e.add(c2)
e.run()

