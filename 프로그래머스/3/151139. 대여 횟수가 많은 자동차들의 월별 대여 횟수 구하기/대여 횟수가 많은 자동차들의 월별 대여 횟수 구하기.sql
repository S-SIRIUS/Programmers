select date_format(START_DATE, "%m")+0 MONTH, CAR_ID, count(*) RECORDS 
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where CAR_ID in 
(select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10' group by CAR_ID having count(CAR_ID)>=5) AND (DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10') 
group by date_format(START_DATE, "%m"), CAR_ID 
having count(*) >0 
order by date_format(START_DATE, "%m") asc, CAR_ID desc;