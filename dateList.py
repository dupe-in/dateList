import numpy as np

# 8자리 시작, 마지막 날짜 입력
startDate = "20220102"
lastDate = "20221231"

syear = startDate[0:4]
smonth = startDate[4:6]
sday = startDate[6:]
strStartDate = syear + "-" + smonth + "-" + sday

lyear = lastDate[0:4]
lmonth = lastDate[4:6]
lday = lastDate[6:]
strLastDate = lyear + "-" + lmonth + "-" + lday

dateStartDate = np.array(strStartDate, dtype=np.datetime64)
dateLastDate = np.array(strLastDate, dtype=np.datetime64)
c = dateLastDate - dateStartDate

resultList = [dateStartDate + np.arange(c + 1)]

print(resultList[0])
