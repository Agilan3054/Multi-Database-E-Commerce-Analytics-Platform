-- Total sales per product
SELECT p.name, SUM(o.quantity) AS total_sales
FROM orders o
JOIN products p ON o.product_id = p.id
GROUP BY p.name
ORDER BY total_sales DESC;
