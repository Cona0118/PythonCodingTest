# 자료형
a = (1,2,3,4,5,6,7,8,9) #  튜플, 소괄호로 선언 및 초기화
this_is_not_tuple = ("Seoul")
print(type(this_is_not_tuple))  # 튜플 주의! 서울은 튜플인가? 타입 출력
this_is_tuple = ("Seoul",)
print(type(this_is_tuple))  # , 콤마를 최소 1개 이상 추가 필요, 타입 출력

print(a[3]) # 네 번째 원소만 출력
print(a[1:4]) # 2~4번째 원소 출력, 인덱스/슬라이싱 지원
print(a[:]) # 전체 원소 출력
print(type(a)) # 현재 자료구조 타입 확인

#a[1] = 'i' 특정 인덱스의 데이터 직접 수정 불가

b = (1, 'apple', 'banana', 3.13, [1, 2, 3, 4, 5]) # 서로 다른 데이터/자료구조 입력
print(b) # 전체 출력

c = tuple(range(1, 10)) # range 함수로 초기화 가능
for c_tuple in c:
    print(c_tuple) # for문으로 loop 순회 출력, 1개씩 접근
print(c) # 전체 출력