select i.ANIMAL_ID, i.NAME from ANIMAL_INS i, ANIMAL_OUTS o where i.ANIMAL_ID = o.ANIMAL_ID and o.DATETIME < i.DATETIME order by i.DATETIME;