# 자료형
dic = dict()  # 빈 사전자료 구조 생성, dict 함수
dic['사과'] = 'Apple' # 키, 값을 가지는 사전 자료구조
dic['바나나'] = 'Banana' # 키, 값을 추가 선언하면 자동 추가됨
dic['코코넛'] = 'Coconut'
dic2 = {'a':123123, (1,1):654321, 1:'banana'} # 한번에 여러 데이터 타입의 사전 선언, 대괄호 사용

print(dic) # 값 전체 출력, 참고 : 인덱싱 사용 X
print(dic2) # 값 전체 출력
print(type(dic)) # 딕셔너리, 사전

if '사과' in dic: # 튜플과 같이 if in, if not in 모두 사용 가능
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

if 'Apple' not in dic: # 튜플과 같이 if in, if not in 모두 사용 가능
    print("'Apple'을 키로 가지는 데이터가 존재하지 않습니다.")