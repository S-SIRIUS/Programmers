select a.APNT_NO, p.PT_NAME, p.PT_NO, d.MCDP_CD, d.DR_NAME, a.APNT_YMD from PATIENT p, DOCTOR d, (select * from APPOINTMENT where date_format(APNT_YMD, "%Y-%m-%d")="2022-04-13" and  APNT_CNCL_YN="N") a where p.PT_NO = a.PT_NO and a.MDDR_ID = d.DR_ID and d.MCDP_CD = "CS" order by a.APNT_YMD;