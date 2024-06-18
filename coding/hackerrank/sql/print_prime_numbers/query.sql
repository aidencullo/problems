declare @start int = 1000
declare @end int = 1050

SELECT DISTINCT n = number 
FROM master..[spt_values] 
WHERE number BETWEEN @start AND @end
