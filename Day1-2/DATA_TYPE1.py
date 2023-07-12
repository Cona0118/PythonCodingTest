# 자료형
a = 1000 # 양수
b = 1.333 # 음수
b_1 = 5. # 실수는 뒤의 0 생략 가능
b_2 = -.733 # 앞의 0도 생략 가능
c = -3333
d = 0
print(a, b, b_1, b_2, c, d) # 정수형 - 양수, 실수, 음수, 0

e = 1e9 # 10억, 지수 표현 10의 x승
e_1 = 175.25e1 # 1752.5 표현
e_2 = 39555e-3 # 39.555 표현
print(e, e_1, e_2) # 지수 출력

a = 0.333 + 0.666 # 실수 합 연산
print(a)

if (a==0.999): # 참 거짓 판단
    print(True)
else:
    print(False)
    
a = 0.333 + 0.666
print(round(a, 4))  # round 반올림 함수
if round(a, 4) == 0.999:
    print(True)
else:
    print(False)
