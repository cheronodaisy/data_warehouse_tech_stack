

with fast_v as (select * from "traffic"."public"."fast_vehicles")

SELECT 
" type" as "Vehicle type",
count(" type") as "vehicle count"
from fast_v 
GROUP BY " type" ORDER BY "vehicle count" ASC