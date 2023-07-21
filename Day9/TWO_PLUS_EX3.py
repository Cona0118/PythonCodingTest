# 문제 : N개의 수로 된 수열 A[1], A[2], ….A[N]이 있다. 이 수열의 i번째 수부터 J번째 수까지의 합이 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
# 참고 : M =  A[i] + A[i+1] + … + A[j-1] + A[j]
# 참고 : 입력 N은 1 ≤ N ≤ 10,000), 합 M은 1 ≤ M ≤ 300,000,000
# 요구사항 : 시간 제한 0.5초, 메모리 128MB

# 입력
# 4 2            10 5
# 1 1 1 1        1 2 3 4 2 5 3 1 1 2
# 출력
# 3              3

# 문제 해결을 위한 아이디어? 반복문(완전탐색)으로? 사실 가능하다. BUT, 투 포인터 개념/코드를 참고하여 부분합을 출력하자.
n,m = map(int,input().split())
array = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += array[end]
        end += 1
 # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= array[start]

print(count)