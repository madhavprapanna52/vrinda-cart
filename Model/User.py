from DB.Execute import executor
from DB.Object import Object

class User:
    def __init__(self, user_id: int):
        self.id = user_id

    def cart_items(self):
        """
        returns all cart items with price & total
        """
        query = "select * from cart_items where user_id = ?"
        return executor(query, (self.id,), fetch=True)

    def cart_total(self):
        """
        returns total cart bill
        """
        query = "select total_amount from cart_bill where user_id = ?"
        result = executor(query, (self.id,), fetch=True)
        return result[0][0] if result else 0.0

    def add_to_cart(self, product_id: int, quantity: int):
        """
        adds new item OR increments existing quantity
        """
        query = """
        insert into cart (user_id, product_id, quantity)
        values (?, ?, ?)
        """
        return executor(query, (self.id, product_id, quantity))

    def update_cart(self, product_id: int, quantity: int):
        """
        sets absolute quantity
        """
        query = """
        update cart
        set quantity = ?
        where user_id = ? and product_id = ?
        """
        return executor(query, (quantity, self.id, product_id))

    def remove_from_cart(self, product_id: int):
        query = """
        delete from cart
        where user_id = ? and product_id = ?
        """
        return executor(query, (self.id, product_id))

    def checkout(self):
        query = "insert into orders (user_id) values (?)"
        return executor(query, (self.id,))

    def order_history(self):
        query = """
        select *
        from order_items_view
        where user_id = ?
        order by created_at desc
        """
        return executor(query, (self.id,), fetch=True)
