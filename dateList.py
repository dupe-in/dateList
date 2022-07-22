import numpy as np

# 시작 날짜와 마지막 날짜
start_date = "20220101"
end_date = "20220215"

# 연도, 월, 일로 끊어서 중간에 '-' 기호 넣기
# 2022-01-01
# str 타입을 date 타입으로 바꾸기 위한 과정
# '-' 기호가 아닌 다른 기호가 올 경우 에러(datetime 때문)

syear = start_date[0:4]
smonth = start_date[4:6]
sday = start_date[6:]
strStartDate = syear + "-" + smonth + "-" + sday

lyear = end_date[0:4]
lmonth = end_date[4:6]
lday = end_date[6:]
strLastDate = lyear + "-" + lmonth + "-" + lday

# 예시 변수 값
# strStartDate = 2022-01-01
# strLastDate = 2022-02-15

# str -> date로 변환
dateStartDate = np.array(strStartDate, dtype=np.datetime64)
dateLastDate = np.array(strLastDate, dtype=np.datetime64)

# c = 날짜간의 차이, date 타입
c = dateLastDate - dateStartDate
# 현재 c의 값
# c = 45 days

# tempList에 시작 날짜부터 마지막 날짜까지 저장
tempList = [dateStartDate + np.arange(c + 1)]

# tempList는 list 타입, 원하는 정보는 0번 인덱스에 있음
tempResult = tempList[0]

# tempResult를 리스트 형태로 변환
changeList = tempResult.tolist()
listLength = len(changeList)

# resultList : 날짜를 append 할 새 리스트
resultList = []

# changeList의 길이만큼 반복
# changeList에 하나씩 접근, 동시에 str타입으로 변환
for i in range(0, listLength):
    resultList.append(str(changeList[i]))

# 결과 출력
print(strStartDate + "부터 " + strLastDate + "까지의 날짜 리스트입니다.\n")
print(resultList)