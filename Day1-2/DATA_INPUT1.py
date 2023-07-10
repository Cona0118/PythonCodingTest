# DAY1 - 입력과 출력

print("정수 또는 문자를 입력해주세요 : ", end='')  # 파이썬은 기본 줄바꿈, end='\n'
n = input()  # 변수 n을 선언과 동시에 입력, input 함수 사용
print(n)  # 변수를 출력, 입력에 따라 데이터 타입이 변화

print(int(n))  # int 정수, str 문자열, float 실수 타입 변환(캐스팅)
