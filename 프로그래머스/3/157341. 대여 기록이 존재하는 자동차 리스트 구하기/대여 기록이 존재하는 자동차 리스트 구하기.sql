select distinct(c.CAR_ID) CAR_ID from CAR_RENTAL_COMPANY_CAR c, CAR_RENTAL_COMPANY_RENTAL_HISTORY h where c.CAR_ID = h.CAR_ID and c.CAR_TYPE="세단" and DATE_FORMAT(h.START_DATE, "%m")=10 order by c.CAR_ID desc; 

/*
select DATE_FORMAT(START_DATE, "%Y%m%d") from CAR_RENTAL_COMPANY_RENTAL_HISTORY;*/
