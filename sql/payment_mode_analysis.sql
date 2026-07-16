SELECT
    PaymentMode,
    COUNT(*) AS TotalTransactions
FROM Transactions
GROUP BY PaymentMode;