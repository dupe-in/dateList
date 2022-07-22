import numpy as np

# 8자리 시작, 마지막 날짜 입력
start_date = "20220102"
end_date = "20220105"

syear = start_date[0:4]
smonth = start_date[4:6]
sday = start_date[6:]
strStartDate = syear + "-" + smonth + "-" + sday

lyear = end_date[0:4]
lmonth = end_date[4:6]
lday = end_date[6:]
strLastDate = lyear + "-" + lmonth + "-" + lday

dateStartDate = np.array(strStartDate, dtype=np.datetime64)
dateLastDate = np.array(strLastDate, dtype=np.datetime64)
c = dateLastDate - dateStartDate

tempList = [dateStartDate + np.arange(c + 1)]
resultList = tempList[0]
resultList = resultList.tolist()
print(resultList)
