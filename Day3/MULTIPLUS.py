# 문제 : 문자열 S가 주어졌을 때 'x' 혹은 '+' 연산으로 가장 큰 수를 구하는 프로그램을 작성하세요. 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.
# 참고 : 각 자리가 숫자(0부터 9)로 이루어짐

num = list(input("입력 : "))
result = 0
for i in num:
    if result <= 1 or int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)
print(result)


data = input('0~9 숫자로 이루어진 문자열 입력 :') 
result = int(data[0]) # 첫 번째 문자를 숫자로 변경하여 대입

for i in range(1, len(data)): # 다음 인덱스~길이까지
    num = int(data[i]) 
    if num <= 1 or result <= 1: # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우 
        result += num # 더하기 수행(먼저)
    else:
        result *= num # 곱하기 수행

print('최종 연산 결과 합산된 수의 크기는 :', result)
