
  create view "traffic"."public"."traffic_details__dbt_tmp"
    
    
  as (
    

with traffic_details as (
  
    SELECT 
    " type" as "Vehicle type",
    count(" type") as "vehicle count",
    Round(AVG(Cast(" traveled_d"  as numeric)),2) as "Avg distance traveled",
    Round(AVG(cast(" avg_speed"  as numeric)),2) as "Avg speed by vehicle"
    from track
    GROUP BY " type"  ORDER BY "vehicle count" ASC
  
)

SELECT * from traffic_details
  );