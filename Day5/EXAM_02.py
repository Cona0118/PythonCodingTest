# 문제 : 주민등록번호를 입력받자. 유효한 주민등록 번호인지 검증하고, 생년월일과 성별을 출력하는 프로그램을 작성하라. 
# 참고 : 입력 YYMMDD-GXXXXXX (YY: 년, MM: 월, DD: 일, G: 성별, X: 번호)
# 참고 : 최근 주민등록번호 뒷자리 지역번호 폐지? – 기존 검증 방법 사용

# 입력 예) 050101-4021511

# 출력 예) 
# 올바른 주민등록 번호입니다. (또는 주민등록 번호 에러!)
# 생년월일 : 2005년01월01일
# 성별 : 여성 (또는 남성)
# 거주지 : 서울
 
date, num = input("주민등록 번호를 입력해주세요: ").split("-") # date == 050101 /  num == 4021511  // 앞자리(생년월일)과 뒷자리 분리

date_list = list(date) # 리스트화
year = ""
month = ""
day = ""
if len(date_list) == 6:
    for i in range(2):
        year = year + date_list[i] 
    if int(date_list[0]) <= 23:
        year = "20"+year # year == 2005
    else:
        year = "19"+year # year == 1995
    
    if int(year) == 0 :
        print("주민등록 번호 에러!")
        exit()
    for i in range(2,4):
        month = month + date_list[i] # month == 01
    if int(month) == 0 or int(month) > 12:
        print("주민등록 번호 에러!")
        exit()
    for i in range(4,6):
        day = day + date_list[i] # day == 01
    if int(day) == 0 or int(day) > 31:
        print("주민등록 번호 에러!")
        exit()
else:
    print("주민등록 번호 에러!")
    exit()

num_list = list(num)
Gender = ""
place = ""
if len(num_list) == 7:
    if num_list[0] == "1" or num_list[0] == "3":
        Gender = "남성"
    elif num_list[0] == "2" or num_list[0] == "4":
        Gender = "여성"
    else:
        print("주민등록 번호 에러!")
        exit()
    
    place_code = int(num_list[1]+num_list[2]) # res_code = 02
    if place_code <= 8:
        place = "서울"
    elif place_code <= 12:
        place = "부산"
    elif place_code <= 15:
        place = "인천"
    elif place_code <= 25:
        place = "경기"
    elif place_code <= 34:
        place = "강원"
    elif place_code <= 39:
        place = "충북"
    elif place_code <= 40:
        place = "대전"
    elif place_code <= 43:
        place = "충청"
    elif place_code <= 44:
        place = "세종"
    elif place_code <= 47:
        place = "충청"
    elif place_code <= 48:
        place = "전북"
    elif place_code <= 49:
        place = "세종"
    elif place_code <= 54:
        place = "전북"
    elif place_code <= 56:
        place = "광주"
    elif place_code <= 66:
        place = "전남"
    elif place_code <= 69:
        place = "대구"
    elif place_code <= 75:
        place = "경북"
    elif place_code <= 76:
        place = "대구"
    elif place_code <= 81:
        place = "경북"
    elif place_code <= 84:
        place = "경남"
    elif place_code <= 85:
        place = "울산"
    elif place_code <= 92:
        place = "경남"
    elif place_code <= 95:
        place = "제주"
    else:
        print("주민등록 번호 에러!")
        exit()
    
else:
    print("주민등록 번호 에러!")
    exit()

print("올바른 주민등록 번호입니다.")
print("생년월일 : %s년%s월%s일"%(year,month,day))
print("성별 :",Gender)
print("거주지 :",place)