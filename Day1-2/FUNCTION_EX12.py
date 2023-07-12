# 문제 : 1,2,3,4,5가 적힌 숫자 카드가 있다. 세 자리 수를 만들 수 있는 방법은? 서로 다른 숫자 5개 중에서 3개를 택하여 일렬로 출력(순열)
# 참고 : 5P3 = 5x4x3 법칙 = 60

from itertools import permutations
data = ['1', '2', '3', '4', '5'] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기

lst =[]

for i in result:
    s = "".join(i)
    lst.append(s)
        
print('모든 순열을 출력 :', lst, len(lst))