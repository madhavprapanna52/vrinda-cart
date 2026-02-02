PRAGMA foreign_keys = ON;

-- Product
CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  price REAL NOT NULL CHECK (price >= 0),
  stock INTEGER NOT NULL CHECK (stock >= 0)
);

-- CART
CREATE TABLE cart (
  user_id INTEGER,
  product_id INTEGER,
  quantity INTEGER NOT NULL CHECK (quantity > 0)
  PRIMARY KEY (user_id, product_id), -- Both are combinedly primary key
  FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

-- order 
CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- view : BILL computation | Making joins and final computation
CREATE VIEW cart_bill AS
SELECT 
  c.user_id,
  SUM(p.price * c.quantity) AS total_amount
FROM cart c
JOIN products p on p.id = c.product_id
GROUP BY c.user_id;

-- Making check at cart addition for preventing un-available stock request
CREATE TRIGGER prevent_negative_stock
BEFORE INSERT ON orders
BEGIN
  SELECT 
    CASE
      WHEN EXISTS (
        SELECT 1
        FROM cart c 
        JOIN products p on p.id = c.product_id
        WHERE c.user_id = NEW.user_id
        AND p.stock < c.quantity
      )
      THEN RAISE(ABORT, 'Insufficient stock')
    END;
END;

CREATE TRIGGER finalize_checkout
AFTER INSERT ON orders
BEGIN
  -- REDUCE STOCK FROM PRODUCTS
  UPDATE products
  SET stock = stock - (
    SELECT quantity
    FROM cart
    WHERE cart.product_id = products.id
    AND cart.user_id = NEW.user_id
  ) -- quantity fetch from cart for updating stock at product level
  WHERE id in (
    SELECT product_id from cart WHERE user_id = NEW.user_id
  );

  -- clear cart
  DELETE FROM cart WHERE user_id = NEW.user_id;
END;
