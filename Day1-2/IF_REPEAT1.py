# DAY1 - 조건문, 반복문
a, b = map(int, input('입력한 두 정수의 큰값 판단 1(3항 연산자) : ').split())
if (a > b): # if문 조건문 활용, a가 b보다 크면 a 출력
    print(a) # 콜론 이후 들여쓰기 필수, 들여쓰기 수준도 같아야함
else: 
    print(b) # 위 조건의 반대, 아닌 경우 b 출력

a, b = input('입력한 두 정수의 큰값 판단 2(3항 연산자) : ').split()
a = int(a) # 정수형 캐스팅
b = int(b) # 정수형 캐스팅
c = a if a>=b else b # 3항 연산자 활용
print(c)

a, b, c = map(int, input('입력한 3개 정수 중 작은값 판단 1').split())
print(min(a,b,c)) # min(작은값) 함수 활용, 참고 : max, avg 등 

a, b, c = map(int,input('입력한 3개 정수 중 작은값 판단 2(3항 연산자)').split())
print((a if (a<b) else b)if ((a if (a<b) else b)<c) else c) # 3항 연산자 활용
