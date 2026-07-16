SELECT
    CAST(OrderDate AS DATE) AS SalesDate,
    COUNT(OrderID) AS TotalOrders,
    SUM(TotalAmount) AS TotalRevenue
FROM Orders
GROUP BY CAST(OrderDate AS DATE)
ORDER BY SalesDate;