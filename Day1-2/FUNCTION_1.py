# 함수
def add(a, b): # def 키워드로 함수 시작을 정의
    print('함수를 호출합니다 : ', a + b) # 내부에서 직접 출력
    return a + b # 합산 결과를 리턴, 리턴 시점에서 함수는 중단됨

print('add 함수를 호출 합니다 : ')
print(add(3, 15)) # 함수 호출 및 매개변수 값 전달 출력
print(add(b=3, a=10)) # 직접 매개변수, 인자값 지정 출력

def add2(a, b):
    a = 25 # 함수 내부 지역변수 선언
    b = 25
    print(a + b)

print('add2 함수를 호출 합니다 : ')
add2(1, 1) # 매개변수 전달 상관없이 a + b 출력

a = 15 # 함수 외부에 전역변수 선언
def add3():
    global a # 전역 변수 적용됨
    b = 25
    print(a + b)

print('add3 함수를 호출 합니다 : ')
add3() # 전역변수 a + b 출력	