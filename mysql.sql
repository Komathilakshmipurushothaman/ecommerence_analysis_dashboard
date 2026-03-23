SELECT 
    o.order_id,
    c.customer_name,
    c.city,
    p.product_name,
    p.category,
    o.order_date,
    o.order_month,
    (p.price * o.quantity) AS total_amount,

    RANK() OVER (
        ORDER BY SUM(p.price * o.quantity) OVER (PARTITION BY c.customer_id) DESC
    ) AS customer_rank,

    COUNT(o.order_id) OVER (
        PARTITION BY o.order_year, o.order_month
    ) AS monthly_orders

FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;