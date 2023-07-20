# 문제 : 큰 수부터 작은 수 순서로 정렬하는 프로그램을 작성하라. 
# 참고 : 입력 : 첫번째 줄에 수열에 속해 있는 수의 개수 N, 두번째 줄부터 N+1 번째 줄에는 N개의 수를 모두 입력. 범위는 1이상 10만 이하의 자연수
# 참고 : 공백 구분, 중복되는 수의 처리 상관없음

# 힌트
# 방식 1 : 기본 파이썬 정렬 라이브러리
# 방식 2 : 퀵 정렬 구현(꼭 해보자!)

N = int(input("숫자의 개수: "))
num = []
for i in range(N):
    num.append(int(input("")))
num.sort(reverse=True)
for i in range(N):
    print(num[i],end = " ")
print("")

N = int(input("숫자의 개수: "))
num = []
for i in range(N):
    num.append(int(input("")))
    
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr)//2]
    low_arr, eq_arr, high_arr = [],[],[]
    for i in arr:
        if i > mid:
            high_arr.append(i)
        elif i < mid:
            low_arr.append(i)
        else:
            eq_arr.append(i)
    return quick_sort(high_arr) + eq_arr + quick_sort(low_arr)

for i in range(N):
    print(quick_sort(num)[i],end = " ")
print("")
            