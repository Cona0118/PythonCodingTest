# 자료형
data = set() # 빈 집합 자료 구조 생성
data = set([1, 2, 23, 3, 5, 77, 5]) # 집합 자료 구조, 초기화 방법 1(set) 함수, 내부 리스트 자료구조
print(data) # 인덱싱 사용 X
data = {1, 1, 2, 3, 4, 4, 5} # 초기화 방법2, 중괄호를 활용
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

data.add(4) # 새로운 원소 추가
print(data)

data.update([5, 6]) # 새로운 원소 여러 개 추가
print(data)

data.remove(3) # 특정한 값을 갖는 원소 삭제
print(data)