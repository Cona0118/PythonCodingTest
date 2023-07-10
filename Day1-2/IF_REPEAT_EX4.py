# 문제 1 : 정수(1 ~ 100) 1개를 입력 받아 1부터 그 수까지 짝수의 합을 출력하시오.
# for, while 문 선택
num = int(input("1부터 100사이의 정수 입력: "))
Sum = 0
for i in range(0,num+1,2):
    Sum += i
print(Sum)

Sum = 0
for i in range(num+1):
    if (i%2 == 0):
        Sum += i
print(Sum)

# 문제 2 : 영문 소문자 q가 입력될 까지 입력 문자를 무한 출력하시오.
# While 문과 if문 활용 
q = input("소문자 알파벳 입력: ")
while q != "q":
    print("입력한 문자 : ",q)
    q = input("소문자 알파벳 입력: ")
print("입력한 문자 : ",q)