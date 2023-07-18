# 문제 : 모험가(1, 1)위치 기준으로 N X M 크기 미로에서 괴물을 피해 탈출해야 합니다. 탈출하기 위한 최소 칸의 개수를 구하시오.
# 참고 : 괴물은 있는 부분 0, 없는 부분 1로 표시
# 참고 : 시작과 마지막 칸 모두 포함해서 개수 계산
n, m =  map(int, input('미로의 크기 입력 :').split()) # (n,m)
maze = []   
for i in range(m):
    print(i+1,"번째 줄 입력(0 or 1): ",end="")
    s = list(input(''))
    maze.append(s)
    
maze[0][0] = "1"
maze[m-1][n-1] = "1" # maze[y][x]

print("")
for i in range(len(maze)):
    for j in range(len(maze[i])):
        print(maze[i][j],end=" ")
    print("")
print("")

for i in range(len(maze)):
    maze[i].append("0")
maze.append(list("0"*(n+1)))

counter = 0
def bfs(a,b): #(a,b)
    queue = [[a-1,b-1]] # [0,0]
    v = [0,0]
    counter = 0
    
    while v[0] != n-1 or v[1] != m-1 :
        v = queue[counter]
        
        if maze[v[1]][v[0]+1] == "1":
            if [v[0]+1, v[1]] not in queue:
                queue.append([v[0]+1, v[1]])
                counter += 1
                    
        elif maze[v[1]+1][v[0]] == "1":
            if [v[0], v[1]+1] not in queue:
                queue.append([v[0], v[1]+1])
                counter += 1
                
        else:
            counter -= 1
            queue.pop()
            maze[v[1]][v[0]] = "0"
                
    result=[]
    for i in range(len(queue)):
        result.append([queue[i][0]+1,queue[i][1]+1])
    result.append([n,m])
    
    print("탈출 경로 :", result)
    print("이동 횟수 :", len(result)-1)
bfs(1,1)

print("======================================================")
# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기, 종료 조건이됨
    while queue: 
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i] # 상, 하, 좌, 우 모두 방문
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 거리 한칸 증가
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

from collections import deque # 큐 자료구조 연동

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0)) # 그래프 상으로는 0, 0 부터 출발
