# 문제 : 소문자 단어 s의 입력에 대해, 각 알파벳(a~z) 26개를 기준으로 입력한 문자의 위치를 출력하는 프로그램을 작성하시오.
# 참고 : 글자는 중복되지 않아야 한다, 포함되어 있지 않는 경우 -1을 출력
# 참고 : 첫 번째 글자는 위치 0, 2번째 글자는 위치 1, 3번째 글자는 2 (계속 증가)

result = []
for i in range(26):
    result.append(-1)
# == result = [-1]*26 

char = input("")
char_array = list(char)

for i in char_array:
    result[ord(i)-97] = char_array.index(i)
    
print(result)