from Product import *

p = Product("laptop", 100, 1)

print("Running tests")
print(f'Get method : {p.get()}')
print(f"fetch information : {p.fetch_info()}")
print(f"Updating information")

p.update(2, 2)
print(f"Update done : {p.fetch_info()}")

