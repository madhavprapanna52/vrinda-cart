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
  created_at text default current_timestamp
);

-- BILL | table with fetching information
create view bill as
select
  c.user_id,
    sum(p.price * c.quantity) as total_amount
  from cart c
  join products as p on p.id = c.product_id
  group by c.user_id;
