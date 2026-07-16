SELECT
    p.ProductName,
    SUM(o.Quantity) AS TotalSold,
    SUM(o.TotalAmount) AS Revenue
FROM Products p
JOIN Orders o
ON p.ProductID = o.ProductID
GROUP BY p.ProductName
ORDER BY Revenue DESC;