SELECT 
    c.city,
    
    -- Aggregations
    COUNT(o.order_id) AS total_orders,
    SUM(o.order_amount) AS total_revenue,
    AVG(o.order_amount) AS avg_order_value,

    -- CASE 
    CASE 
        WHEN AVG(o.delivery_time_minutes) <= 30 THEN 'Fast City'
        WHEN AVG(o.delivery_time_minutes) <= 45 THEN 'Moderate City'
        ELSE 'Slow City'
    END AS delivery_performance,

--  Window Function: Rank Cities by Revenue
    RANK() OVER (ORDER BY SUM(o.order_amount) DESC) AS city_rank,

    -- Window Function: Running Total Revenue
    SUM(SUM(o.order_amount)) OVER (ORDER BY SUM(o.order_amount) DESC) AS running_revenue

FROM orders o

-- JOIN
INNER JOIN customers c
ON o.customer_id = c.customer_id

-- GROUP BY
GROUP BY c.city;