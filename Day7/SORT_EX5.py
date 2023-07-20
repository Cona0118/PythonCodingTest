# 문제 : 전자매장에 부품이 N개가 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 내일 M개 종류의 부품을 대량으로 납품해야 한다. 
#        매장 내에 모든 부품을 확인하는 프로그램을 작성하자.
# 참고 : 입력 N = 5종류, 8 3 7 9 2를 보유,  손님 M = 3종류, 5 7 9 부품을 찾음

# 요구사항 : 시간 제한 1초, 메모리 제한 128MB
# 이진 탐색에 들어가는 리스트는 미리 정렬 필요
# 손님이 찾는 m개의 target이 N에 존재하는지 탐색
# 반복문, 재귀, bisect 라이브러리 등 다양하게 접근 가능

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))
M_list.sort()


for i in range(M):
    if M_list[i] in N_list:
        print("Yes",end=" ")
    else:
        print("No",end=" ")
        
import sys
from bisect import bisect_left

si = sys.stdin.readline
n = int(si())
store = sorted(map(int, si().split())
m = int(si())
wish = list(map(int, si().split()))
               
for x in wish:
    idx = bisect.bisect_left(store,x)
    if store[idx] == x:
        print("yes",end =" ")
    else:
        print("no",end =" ")