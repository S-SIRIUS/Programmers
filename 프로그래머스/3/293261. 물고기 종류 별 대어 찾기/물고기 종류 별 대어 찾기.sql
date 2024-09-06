select f.ID, n.FISH_NAME, f.LENGTH from FISH_INFO f, FISH_NAME_INFO n, (select f.FISH_TYPE, max(f.LENGTH) LENGTH from FISH_INFO f, FISH_NAME_INFO n where n.FISH_TYPE = f.FISH_TYPE group by f.FISH_TYPE) big where f.FISH_TYPE = n.FISH_TYPE and f.FISH_TYPE = big.FISH_TYPE and f.LENGTH = big.LENGTH; 