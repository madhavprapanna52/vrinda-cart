
-- stock out prevention | If product stock insufficient stop checkout
create trigger prevent_checkout_insufficient_stock
before insert on orders
begin
	select
		case
			when exists(
			select 1
			from cart c
			join products p on p.id = c.product_id
			where c.user_id = new.user_id
			and p.stock < c.quantity -- if less stock detected prevent checkout
		)
		then raise(abort, 'Insufficient stock')
		end;
end;


-- Checkout finalization unit for authentic transactions
create trigger finalize_checkout
after insert on orders
begin
	-- fetch information from cart and add cart items into order table
	insert into order_items (user_id, product_id, quantity, price_at_purchase)
	select
		c.user_id,
		c.product_id,
		c.quantity,
		p.price
	from cart c
	join products p on p.id = c.product_id
	where c.user_id = new.user_id;

	-- Reduce stock from product table
	update products
	set stock = stock - (
		select c.quantity
		from cart c
		where c.product_id = products.id
		and c.user_id = new.user_id
	)
	/*
	Loop turns for deducting quantity value of cart
	Existing product id in cart with user_id inserted into orders
	*/
	where exists(
		select 1 from cart
		where cart.product_id = products.id
		and cart.user_id = new.user_id
	);
	
	-- clear cart
	delete from cart where user_id = new.user_id;
end;

