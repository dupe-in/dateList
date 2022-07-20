import datetime

# 8자리 시작, 마지막 날짜 입력
startDate = "20220101"
lastDate = "20221231"
intstartDate = int(startDate)
intlastDate = int(lastDate)

# 각 날짜를 리스트에 끊어서 저장
# ex) 20220627 = ['2', '0', '2', '2', '0', '6', '2', '7']
start_dateList = []
for y in (startDate):
    start_dateList.append(y)
last_dateList = []
for y in (lastDate):
    last_dateList.append(y)

# string 타입의 리스트를 int 타입으로 변환
start_dateList = list(map(int, start_dateList))
last_dateList = list(map(int, last_dateList))

# 시작 날짜 정리
thousand = start_dateList[0] * 1000
hundred = start_dateList[1] * 100
yten = start_dateList[2] * 10
yone = start_dateList[3]
mten = start_dateList[4] * 10
mone = start_dateList[5]
dten = start_dateList[6] * 10
done = start_dateList[7]
startYear = thousand + hundred + yten + yone
startMonth = mten + mone
startDay = dten + done

# 마지막 날짜 정리
thousand = last_dateList[0] * 1000
hundred = last_dateList[1] * 100
yten = last_dateList[2] * 10
yone = last_dateList[3]
mten = last_dateList[4] * 10
mone = last_dateList[5]
dten = last_dateList[6] * 10
done = last_dateList[7]
lastYear = thousand + hundred + yten + yone
lastMonth = mten + mone
lastDay = dten + done

# datetime으로 적용
startday = datetime.date(startYear, startMonth, startDay)
lastday = datetime.date(lastYear, lastMonth, lastDay)

# 두 날짜간 차이 계산
dateResult = startday - lastday
dateResult = abs(dateResult)

# 날짜형 -> 문자형 변환 후 날짜간 차이를 정수형으로 저장
strDate = str(dateResult)
sstrDate = strDate.split(' ')
dateGap = int(sstrDate[0])      # 날짜간 차이(정수형)

# 인덱스 번호로 n월에 접근하기 위해 0번 인덱스에 0 삽입
#          1월 2월 3월 4월  5월 6월 7월 8월 9월 10월 11월 12월
mList = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sM = startMonth
sD = startDay

resultList = []
count = 0

for i in range(0, dateGap + 1):     # 1일 ~ 216일
    if i == 0:        
        resultList.append(intstartDate)
    else:
        intstartDate += 1
        sD += 1
        resultList.append(intstartDate)
        if sD == mList[sM]:         # 만약 달의 마지막 날이라면
            sM += 1                 # 달 하나 더하기
            sD = 1                  # 1일로 초기화
            if sM == 3:                     # 2월-3월
                intstartDate += 73
            elif sM % 2 == 1 and sM < 8:    # 4월-5월 / 6월-7월
                intstartDate += 71
            elif sM % 2 == 0 and sM > 9:    # 9월-10월 / 11월-12월
                intstartDate += 71
            elif sM % 2 == 0 and sM > 7:    # 7월-8월
                intstartDate += 70
            elif sM % 2 == 0 and sM < 9:    # 1월-2월 / 3월-4월 / 5월-6월
                intstartDate += 70
            elif sM % 2 == 1 and sM > 8:    # 8월-9월 / 10월-11월
                intstartDate += 70
            if intstartDate == 20221301:
                break
            resultList.append(intstartDate)
    count += 1
    if count == dateGap:
        break

print(resultList)