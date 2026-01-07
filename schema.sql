-- Create product schema
CREATE TABLE IF NOT EXISTS products (
  id INTEGER  PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  prize INTEGER NOT NULL,
  stock INTEGER NOT NULL
);


-- USER entity
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	wallet INTEGER NOT NULL,
	cart TEXT
);

-- Tracing user history and storing purchase records
CREATE TABLE IF NOT EXISTS transactions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_id TEXT NOT NULL,
	customer_id TEXT NOT NULL
)
