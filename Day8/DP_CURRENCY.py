n, m = map(int, input().split())  # 정수 N, M을 입력 받기

array = []
for i in range(n):
    array.append(int(input()))  # N개의 화폐 단위 정보를 입력받기

d = [10001] * (m + 1)  # DP 테이블 초기화
# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    print("인덱스번호 :", i)
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
            print(d[j], d[j - array[i]] + 1)  # 디버그용
            d[j] = min(d[j], d[j - array[i]] + 1)
# 계산된 결과 출력
if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print("최종", d[m])
