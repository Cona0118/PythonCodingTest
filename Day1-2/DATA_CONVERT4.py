# DAY1 - 변환과 연산자
a, b = input('입력한 수의 거듭제곱을 출력 : ').split()
a = int(a)
b = int(b)
print(a**b) # a의 b 거듭제곱 출력
print(pow(a,b)) # pow 거듭제곱 함수로 출력

a, b = input('입력한 두 정수를 비교 : ').split()
a = int(a)
b = int(b)
print(a<b) # 비교연산자 활용, 참(true), 거짓(false) 출력
print(a==b) # 비교연산자 활용, 참(true), 거짓(false) 출력

n = int(input('정수인지 아닌지 판단 : '))
print(bool(n)) # bool 함수로 출력, 참(true), 거짓(false) 출력
print(not n) # not 함수로 출력, 결과의 반대를 출력
print(bool(int(a)) or bool(int(b))) # 한개라도 참인 경우 참(true) 출력
print(bool(int(a)) and bool(int(b))) # 둘다 참인 경우 참(true) 출력
