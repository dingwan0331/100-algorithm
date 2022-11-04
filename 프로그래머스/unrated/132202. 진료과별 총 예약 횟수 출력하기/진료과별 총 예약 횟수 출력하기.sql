-- 코드를 입력하세요
SELECT MCDP_CD as '진료과코드' , count(APNT_YMD) as '5월예약건수'
from APPOINTMENT  
where date_format(APNT_YMD , '%Y-%m') = '2022-05'
group by MCDP_CD
order by 5월예약건수 , 진료과코드

# SELECT MCDP_CD AS '진료과코드',COUNT(*) AS '5월예약건수'
# FROM APPOINTMENT
# WHERE date_format(APNT_YMD,'%m') = '05'
# GROUP BY MCDP_CD
# ORDER BY '5월예약건수' ASC, '진료과코드' ASC
# SELECT * FROM APPOINTMENT 
# WHERE MONTH(APNT_YMD) =5
# AND APNT_CNCL_YN ='N' 
# OR APNT_CNCL_YN IS NULL
# GROUP BY APNT_YMD