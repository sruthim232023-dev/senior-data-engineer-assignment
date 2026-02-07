-- Query to extract total quantities per customer aged 18-35
-- Rule: Omit items with 0 quantity and ensure integer output
SELECT 
    c.customer_id AS Customer, 
    c.age AS Age, 
    i.item_name AS Item, 
    CAST(SUM(o.quantity) AS INTEGER) AS Quantity
FROM Customer c
JOIN Sales s ON c.customer_id = s.customer_id
JOIN Orders o ON s.sales_id = o.sales_id
JOIN Items i ON o.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35
GROUP BY c.customer_id, i.item_id
HAVING Quantity > 0;
