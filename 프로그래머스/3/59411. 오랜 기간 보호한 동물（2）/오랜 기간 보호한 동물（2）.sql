select i.ANIMAL_ID, i.NAME from ANIMAL_INS i, ANIMAL_OUTS o where i.ANIMAL_ID = o.ANIMAL_ID order by (o.DATETIME - i.DATETIME) desc limit 2;