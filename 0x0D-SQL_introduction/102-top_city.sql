-- Displays the top 3 of cities tempes during July and August ordered by temp(desce).
SELECT `city`, AVG(`value`) AS 'avg_temp'
FROM `temperatures`
WHERE `month` = 7 or `month`= 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
