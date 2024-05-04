
/*
  A dbt model to calculate the fastest vehicles
*/

{{ config(materialized='view') }}

with fast_vehicles as (
    SELECT *
    from track
    ORDER BY " avg_speed"  DESC
    LIMIT 50

)


SELECT * FROM fast_vehicles