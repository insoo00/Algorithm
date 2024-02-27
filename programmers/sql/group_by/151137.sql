#1
SELECT car_type, count(*) as cars
from car_rental_company_car
where options like '%시트%'
group by car_type
order by car_type

#2 
SELECT car_type, count(*) as cars
from car_rental_company_car
where options REGEXP '통풍시트|열선시트|가죽시트'
group by car_type
order by car_type