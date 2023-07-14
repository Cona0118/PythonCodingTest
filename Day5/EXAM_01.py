# 문제 : 특정 숫자에서 X개를 제거하여 가장 큰 숫자 출력하는 프로그램을 완성하라. 
#        예) 1231에서 두 수를 제거하면 12, 13, 11, 21, 23, 31을 만들 수 있다. 이중 가장 큰 숫자는 31이다. 
# 참고 : 입력 - 문자열 숫자 S, 제거 숫자 개수 X
# 참고 : S는 2자리 이상 정수, X는 1이상 자연수

# 입력 예) 1942 			출력 : 94
# 입력 예) 1234 			출력 : 34
# 입력 예) 111212412251 	출력 : 4251

S = input("숫자 입력: ")
S_list = list(S) # 입력받은 숫자 리스트로

X = int(input("제거할 숫자의 수 입력: "))

from itertools import combinations 
new_list = list(combinations(S_list, len(S_list)-X)) # X개를 뽑는 모든 조합 구하기
# S자리수 C (S의 자리수 - X) 를 통하여 X개 만큼 숫자를 제외한 모든 경우의 수 구하기 가능
MAX_num = 0
for i in range(len(new_list)): # 조합의 수 만큼 반복
    new_num = "".join(new_list[i]) # (1,2) -> 12
    if MAX_num < int(new_num): 
        MAX_num = int(new_num) # 최대값 구하기
print("최대값은:",MAX_num)