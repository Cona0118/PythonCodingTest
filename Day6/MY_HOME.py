#문제 : 아파트 단지 지도를 입력하여 단지의 개수와 단지 별로 집의 개수를 출력하는 프로그램을 작성하시오.
#참고 : 집은 1, 집이 아닌 곳 0으로 표시 / 연결된 아파트는 같은 단지를 의미
# 요구사항 : 시간 제한 1초, 메모리 제한 129MB
import time
import os
import psutil


n = int(input("N : "))
house = []

for i in range(n):
    print(i+1,"번째 줄 입력(0 or 1): ",end="")
    s = list(input(''))
    house.append(s)

print("")
for i in range(len(house)):
    for j in range(len(house[i])):
        print(house[i][j],end=" ")
    print("")
print("")

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

for i in range(len(house)):
    house[i].append("0")
house.append(list("0"*(n+1)))

visit = [[False] * (n+1) for i in range(n+1)]
counter = 0
h_counter = 0

def house_check(a,b):
    global h_counter
    if not visit[a][b]:
        visit[a][b] = True
        if house[a][b] == "1":
            
            if not visit[a+1][b] and house[a+1][b] == "1":
                    house_check(a+1,b)
            if not visit[a][b+1] and house[a][b+1] == "1":
                    house_check(a,b+1)
                    
house_count = []
for i in range(n):
    for j in range(n):
        if not visit[i][j] and house[i][j] == "1":
            counter += 1
            house_check(i,j)
            house_count.append[h_counter]
        
print("단지의 수 :",counter)
print(house_count)

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print("MB bytes :", process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력

print("==================답=================")
def DFS(x,y,L):
    dx = [-1, 0, 1, 0] # 4가지 방향 정의
    dy = [0, 1, 0, -1]

    for i in range(4): # 상하좌우 검사
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1: # 새로운 집 발견
            arr[nx][ny]=0
            cnt_arr[L]+=1 # 다음 좌표 설정
            DFS(nx,ny,L) # DFS 재귀 호출
            
n = int(input('단지의 크기 N를 입력 : '))
arr = [list(map(int,input('단지 지도 세부 정보를 입력 : '))) for _ in range(n)]
total_cnt = 0 # 단지의 숫자 
cnt_arr=list() # 단지안에 속하는 집의 수 

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            arr[i][j]=0
            cnt_arr.append(1) # 초기 방문 표시
            DFS(i,j,total_cnt) # DFS 탐색 시작
            total_cnt += 1
print('총 단지수 :', total_cnt)
cnt_arr.sort() 
for i in cnt_arr:
    print('각 집의 개수 :', i)

    
