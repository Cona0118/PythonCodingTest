# 문제 : N개 원소 포함한 수열이 오름차순으로 정렬되어 있다.  X가 등장하는 횟수를 계산하는 프로그램을 작성하자. 
# 참고 : 입력 첫번째는 정수 N과 X 입력, 둘째줄은 원소들을 입력
# 힌트 : 예제) 소스코드 BINARY_2.py를 참고한다.

N, X = list(map(int, input().split()))
num = list(map(int, input().split()))

target_count = 0
def count_target(arr, target):
    global target_count
    
    if len(arr) < 1:
        return target_count
    if len(arr) == 1:
        if arr[0] == target:
            target_count += 1
            return target_count
        else:
            return target_count
        
    mid = arr[len(arr)//2]
    
    if mid > target:
        count_target(arr[:len(arr)//2], target)
    elif mid < target:
        count_target(arr[len(arr)//2 + 1:], target)
    else:
        target_count += 1
        count_target(arr[:len(arr)//2], target)
        count_target(arr[len(arr)//2 + 1:], target)
        
count_target(num, X)
if target_count == 0:
    print(-1)
else: 
    print(X,"의 갯수:",target_count)