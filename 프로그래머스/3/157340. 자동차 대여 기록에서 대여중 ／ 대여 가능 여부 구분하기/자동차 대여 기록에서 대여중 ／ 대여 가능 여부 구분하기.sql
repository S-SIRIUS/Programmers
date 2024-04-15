select CAR_ID,
    CASE
        WHEN CAR_ID in (select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY where '2022-10-16' between date_format(START_DATE, "%Y-%m-%d") and date_format(END_DATE, "%Y-%m-%d")) then '대여중'
        ELSE '대여 가능'
    END as "AVAILABILITY"
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by CAR_ID desc;

    