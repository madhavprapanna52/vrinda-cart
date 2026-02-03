pragma foreign_keys = ON;

-- Basic table setup

create table products(
  id integer primary key,
  name text not null unique,
  price real not null check(price >= 0),
  stock integer not null check(stock >= 0)
);

create table cart(
  user_id integer,
  product_id integer,
  quantity integer not null check(quantity >= 0),
  primary key (user_id, product_id),
  foreign key (product_id) references products(id)
);

create table users(
  id integer primary key autoincrement,
  name text unique not null,
  password text not null
);

create table orders(
  id integer primary key  autoincrement,
  user_id integer not null,
  created_at text default current_timestamp,
  foreign key (user_id) references users(id)
);

create table order_items(
	order_id integer not null,
	user_id integer not null,
	product_id integer not null,
	quantity integer not null,
	price_at_purchase real not null,
	
	foreign key (order_id) references orders(id),
	foreign key (user_id) references users(id),
	foreign key (product_id) references products(id)
);

/*
Bill computation
fetch cart instances and product instance
compute the total with making computation and group them with user_id
*/

create view cart_bill as
select
  c.user_id,
  round(sum(p.price * c.quantity), 2) as total_amount
	from cart c
	join products p on p.id = c.product_id
	group by c.user_id;

-- stock out prevention during checkout
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

-- Final checkout : Order insertion based logic
create trigger finalize_checkout
after insert on orders
begin
	-- storing history
	insert into order_items (order_id, user_id, product_id, quantity, price_at_purchase)
	select
		new.id,
		c.user_id,
		c.product_id,
		c.quantity,
		p.price
	from cart c
	join products p on p.id = c.product_id
	where c.user_id = new.user_id;

	-- Reduce stock
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
