# 문제 : N x M 크기의 얼음틀이 있다. 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# 참고 : 구멍이 뚫린 부분은 상, 하, 좌, 우로 붙어있는 경우 연결된 것으로 간주한다



m, n =  map(int, input('가로,세로 입력 :').split())

Ice_frame = []
for i in range(n):
    Ice_frame.append([0]*m)
    
for i in range(n):
    print(i+1,"번째 줄 입력(0 or 1): ",end="")
    s = input('').split()
    Ice_frame[i] = s
    
print()
for i in range(len(Ice_frame)):
    for j in Ice_frame[i]:
        print(j,end=" ")
    print()
print()

visited = []
for i in range(n):
    visited.append([False] * m)

ice_count = 0
def frame_check(a, b):
    global Ice_frame
    global visited
    visited[a][b] = True
    if Ice_frame[a][b] == "0":
        if a - 1 >= 0 and not visited[a - 1][b]:
            frame_check(a - 1, b)
        if a + 1 < n and not visited[a + 1][b]:
            frame_check(a + 1, b)
        if b - 1 >= 0 and not visited[a][b - 1]:
            frame_check(a, b - 1)
        if b + 1 < m and not visited[a][b + 1]:
            frame_check(a, b + 1)
    
    
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if Ice_frame[i][j] == "0":
                frame_check(i,j)
                ice_count += 1
            else:
                visited[i][l] = True

print(ice_count)

print("------------------------------------------")
# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y): // 가로, 세로
    # 얼음틀에서 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0: # 처음엔 0, 0
        # 해당 노드 방문 처리, 얼음 표시
        graph[x][y] = 1 # 방문 이후 1, 1
        # 상, 좌, 하, 우의 위치 재귀 호출(모든 방향 탐색)
        dfs(x - 1, y) 
        dfs(x, y - 1) 
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True # 방문 끝나면 참 리턴
    return False # 재귀 탈출 조건

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력

