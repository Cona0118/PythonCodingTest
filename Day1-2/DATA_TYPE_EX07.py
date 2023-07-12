# 문제 : 리스트에 문자열을 저장하고 출력	
# 리스트 [] 선언, append 함수(내용 추가) 활용
# While문 내에서 입력 받기 : if 엔터( ‘ ‘ ) 누르면 정지
# 리스트 컴프리핸션 전체 출력 : for문

a = ["string", "문자열"]
print(a)

b = input("내용 추가 : ")
while b != "":
    a.append(b)
    b = input("내용 추가 : ")

result = [i for i in a]
print(result)