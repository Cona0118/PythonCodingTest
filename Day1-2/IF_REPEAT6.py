# DAY1 - 조건문, 반복문
c=input('A부터 입력한 문자까지 순서대로 출력 : ')
i = ord('a') # a의 아스키코드 정수 값 65
c = ord(c)
while i<=c: # a부터 입력한 문자 정수 값까지 
    print(chr(i), end=' ') # chr 캐스팅하여 문자 출력, 줄바꿈 x
    i+=1 # i = i + 1과 같음, 1씩 증가
    
print()

a = int(input('정수 1개 입력받아 그 수까지 출력 : '))
for i in range(0, a+1): # 처음부터 a + 1까지, n + 1도 가능
    if i%2==0:
        continue # 특정 조건 실행을 건너뛸 때 사용     
    print(i) # 값 출력
