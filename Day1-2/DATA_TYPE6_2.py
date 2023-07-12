# 자료형
dic3 = {'key':'문자열데이터 값', (3,3):654321, 999:'apple'} # 한번에 여러 데이터 타입의 사전 선언, 대괄호 사용
print(f'dic3["key"] = {dic3["key"]}') # 파이썬 포맷팅 - f-string 문법으로 출력
print({dic3["key"]}) # 키 값에 대한 데이터 출력
print({dic3[(3,3)]}) # 키 값에 대한 데이터 출력

dic3["hello"] = 2022   # 사전에 새로운 데이터 추가
dic3[999] = 'banana'   # 999키 값의 데이터 수정

del dic3["key"] # 사전의 키 값으로 자료 삭제
print(dic3) # 삭제 후 사전 전체 출력

print()
key_list = dic3.keys() # 키 데이터만 담은 리스트
value_list = dic3.values() # 값 데이터만 담은 리스트
print(key_list) # 키 정보 전체 출력
print(value_list) # 값 정보 전체 출력

for key in key_list:
    print(dic3[key]) # 각 키에 따른 값을 하나씩 출력