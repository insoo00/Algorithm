SELECT cc.car_id, cc.car_type, FLOOR((cc.daily_fee*30*(1-dp.discount_rate/100))) as FEE
FROM CAR_RENTAL_COMPANY_CAR as cc
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY as rh ON cc.car_id = rh.car_id
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as dp ON cc.car_type = dp.car_type
WHERE cc.car_type in ('세단', 'SUV')
# AND start_date not between '2022-11-01' and '2022-11-30'
# AND end_date not between '2022-11-01' and '2022-11-30'
and cc.car_id NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE > '2022-11-01' AND START_DATE < '2022-12-01'
)
AND duration_type = '30일 이상'
AND (cc.daily_fee*30*(1-dp.discount_rate/100)) between 500000 and 2000000
GROUP BY cc.car_id
order by fee desc, cc.car_type, cc.car_id desc;