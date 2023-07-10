# DAY1 - 조건문, 반복문
n=int(input('정수 1개 입력받아 분류하기 : '))
if n < 0: # 0보다 작으면 음수
    if n % 2==0: # if문 안에 if문 중첩
        print('음수, 짝수 : A')
    else:
        print('음수, 홀수 : B')
else: # 아닌 경우 양수
    if n % 2==0: # if문 안에 if문 중첩
        print('양수, 짝수 : C')
    else:
        print('양수, 홀수 : D')
          
a=int(input('점수 입력받아 평가 출력하기 : '))
if a>=90:
    print("A학점") 
elif a>=70: # elif는 else if의 약어, 들여쓰기 없어 가독성 굿
    print("B학점")
elif a>=40:
    print("C학점")
else:
    print("D학점")



