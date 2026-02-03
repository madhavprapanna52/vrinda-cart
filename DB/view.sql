
-- select * from cart_bill where user_id = ? | user total
create view cart_bill as
select
  c.user_id,
  round(sum(p.price * c.quantity), 2) as total_amount
  from cart c
  join products p on p.id = c.product_id
  group by c.user_id;


-- cart_items select * from cart_items where user_id = ?
create view cart_items as
select
  c.user_id,
  c.product_id,
  p.name as product_name,
  c.quantity,
  p.price as product_price,
  round(c.quantity * p.price, 2) as total
from cart c 
join products p on p.id = c.product_id;

-- Order history fetch select * from order_items_view where user_id = ? 
create view order_items_view as
select
  o.id as order_id,
  o.user_id as user_id,
  o.created_at,
  p.name as product_name,
  oi.quantity as quantity,
  oi.price_at_purchase price
  from orders o
  join order_items oi on oi.order_id = o.id
  join products p on p.id = oi.product_id;


