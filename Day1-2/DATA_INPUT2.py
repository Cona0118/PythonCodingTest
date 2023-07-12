# DAY1 - 입력과 출력
print("첫번째 정수를 입력해주세요 : ", end='')
a = input()
print("두번째 정수를 입력해주세요 : ", end='')
b = input()
print(a, b)  # 두 변수를 한번에 출력
print(b, a)  # 두 변수를 순서 교체 후 한번에 출력


# 중요
print("한번에 문자를 2번 입력받습니다 : ", end='')
c, d = input().split()  # 문자 2개 입력, 공백 기준 분리, 정수형 map(int, input.split()), 실수형 map(float, input.split())
print(c, d)  # 두 변수를 한번에 출력
 