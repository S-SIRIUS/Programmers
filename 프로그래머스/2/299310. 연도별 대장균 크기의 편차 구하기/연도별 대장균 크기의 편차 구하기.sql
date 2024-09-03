select YEAR(e.DIFFERENTIATION_DATE) as YEAR, (s.maxi - e.SIZE_OF_COLONY) as YEAR_DEV, e.ID 
from (select YEAR(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) maxi from ecoli_data group by YEAR(DIFFERENTIATION_DATE)) s, ecoli_data e 
where s.YEAR = YEAR(e.DIFFERENTIATION_DATE)
order by YEAR, YEAR_DEV;