select substring(PRODUCT_CODE,1,2)  CATEGORY, count(*) PRODUCTS from PRODUCT group by substring(PRODUCT_CODE,1,2) order by PRODUCT_CODE;