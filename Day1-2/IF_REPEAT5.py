# DAY1 - 조건문, 반복문
while True:
    a=input('0이 입력될 때까지 무한 반복 : ')
    a=int(a)
    if (a == 0): # 0인 경우
        break # 현재 반복문을 중단
    else:
        print(a) # 출력 반복
        
a=int(input('입력 한 정수 카운트 다운 출력 1 : '))
while a!=0: # 정수가 입력되면 동작 시작
    print(a)
    a=a-1 # a변수에 1씩 뺀 후 저장
    
a = int(input('입력 한 정수 카운트 다운 출력 2 : '))
while True: # 무조건 동작 시작
    a = a - 1 # 출력 이전 1씩 뺀 후 저장
    print(a) # -1된 값 먼저 출력, 0까지 출력
    if (a <= 0): # 0인 경우 
        break # 현재 반복문을 중단







