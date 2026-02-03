-- Schema sql

create table products(
  id integer primary key autoincrement,
  name text not null unique,
price real not null check(price >= 0),
  stock integer not null check(stock >= 0)
);


create table cart(
  id integer primary key autoincrement,
  user_id integer,
  product_id integer,
  quantity integer not null check(quantity >= 0),

  foreign key (user_id) references users(id),
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
	order_id integer primary key autoincrement,
	user_id integer not null,
	product_id integer not null,
	quantity integer not null,
	price_at_purchase real not null,
	
	foreign key (order_id) references orders(id),
	foreign key (user_id) references users(id),
	foreign key (product_id) references products(id)
);


