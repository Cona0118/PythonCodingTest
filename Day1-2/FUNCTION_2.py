# 함수
def operator(a, b): # def 키워드로 함수 시작을 정의
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var # 리턴 여러개 가능

a, b, c, d = operator(7, 3) # 사칙 연산 함수 호출
print('4칙 연산 함수를 호출 합니다 : ')
print(a, b, c, d)

def gugudan(num): # 구구단 함수 정의
    for i in range(1, 10): # for문 활용, 1~9까지
        print(f'구구단을 출력합니다 : {num} x {i} = {num * i}') # f-string 기법 적용
    
gugudan(3) # 3단 구구단 출력
