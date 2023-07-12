# 자료형
n = 4
m = 3
array = [[0] * m for _ in range(n)]  # N X M 크기의 2차원 리스트 초기화 : 대괄호, 리스트 컴프리헨션
print(array)
print(type(array)) # 현재 자료구조 타입 확인

array[2][1] = 5
print(array)

a = [1, 4, 3]
print("기본 리스트: ", a)

a.append(2) # 리스트에 원소 삽입
print("삽입: ", a)

a.sort() # 오름차순 정렬
print("오름차순 정렬: ", a)

a.sort(reverse = True) # 내림차순 정렬
print("내림차순 정렬: ", a)