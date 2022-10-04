/*
 * 풀이
 * https://whimsical-report-4b5.notion.site/77487-29aea44adf274122ba64cf68739e035b
 */

SELECT * FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) >= 2
)
ORDER BY ID;