# DAY1 - 조건문, 반복문
a = input('A, B, C, D 문자에서 1개를 입력 : ')
if (a == "A"): # 문자열 비교
    print("A : best!!!")
elif (a == "B"): # elif는 else if의 약어
    print("B : good!!")
elif (a == "C"):
    print("C : run!")
elif (a == "D"):
    print("D : slowly~")
else:
    print("what?")
    
a=int(input('1~12 사이 숫자 입력하여 월 판단 : '))
if a//3==1: # 3으로 나눠 몫이 1이면 봄(3, 4, 5)
    print("spring")
elif a//3==2: # 3으로 나눠 몫이 2이면 봄(6, 7, 8)
    print("summer")
elif a//3==3: # 3으로 나눠 몫이 3이면 봄(9, 10, 11)
    print("fall") 
else: # 아니면 겨울(12, 1, 2)
    print("winter")
