# DAY1 - 조건문, 반복문
a, b, c = input('정수 3개를 입력받아 짝수를 출력 : ').split()
a=int(a)
b=int(b)
c=int(c)

if a%2==0: # 2로 나눠지면 출력
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)
    
s = map(int, input('정수 3개를 입력받아 짝수를 출력(for문) : ').split())
for i in s: # s의 첫 요소부터 끝까지 대입
    if i % 2 == 0: # 2로 나눠지면 출력
        print(i)
