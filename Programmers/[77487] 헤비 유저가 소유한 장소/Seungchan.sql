select * from places where HOST_ID in (select HOST_ID from (select HOST_ID, count(HOST_ID) as cnt from places group by HOST_ID) as NEW where cnt>=2)
