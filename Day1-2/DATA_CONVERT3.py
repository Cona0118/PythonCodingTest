# DAY1 - 변환과 연산자
f = float(input('소수점 5자리 이하 입력 : '))
print(round(f,2)) # 소수점 2자리 출력, round는 반올림 함수
# 팁(tip) : Round 함수 주의 - 0.5는 0.5 출력, 중간 값은 반올림 하지 않음

a=input('소수를 5자리 이하 입력 : ')
a=float(a) # 입력값 소수로 캐스팅
print(format(a, ".2f")) # format 함수 소수점 2자리 출력

a, b = map(float, input('소수 5자리 이하 2개 입력 : ').split()) # 실수 2개 입력 받음
c = a/b
print("%0.3f" %c) # 소수점 3자리 출력

a, b, c = input('정수를 3개 입력 : ').split() # 정수 3개 입력 받음
a=int(a)
b=int(b)
c=int(c)
total=a+b+c # 변수에 합 저장
avg=total/3 # 변수에 평균 저장
print(total, format(avg, ".2f")) # 합산 결과와 평균(소수점 2자리) 출력
