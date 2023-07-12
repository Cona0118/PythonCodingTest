# 자료형
b = (2, 'bakery', 'coffee', 3.13, [5, 4, 3, 2, 1]) # 서로 다른 데이터/자료구조 입력
b = b + (1.3, 'name', 5) # 데이터 변경 방법 1, but 변경된 것이 아님(새로 생성됨)
t_length = len(b) # 튜플의 길이 len 함수
print(t_length) # 튜플의 길이를 출력
print(b) # 전체 출력

lst = list(b) # 데이터 변경 방법 2, 리스트로 변환 내용 수정
lst.append('add') # 리스트 내용 추가
c = tuple(lst) # 리스트를 튜플로 변환
print(c) # 전체 출력
del c # del 키워드로 튜플 삭제

if 'coffee' in b: # if in으로 특정 데이터 존재 확인
    print('커피가 존재합니다.')
if '3.333' not in b: # if not in으로 특정 데이터가 존재하지 않는지 확인
    print("3.333은 존재하지 않습니다.")

d = (3, 4444, (55, 55), 6) # 튜플내 자료 중첩도 가능
print(d) # 전체 출력
          