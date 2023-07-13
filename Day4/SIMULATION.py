# 문제 : 모험가 A가 N의 공간에서 계획서에 따라 이동하는 경우, 최종 도착하는 좌표의 (X, Y)를 출력하시오.
# 참고 : N X N의 2차원 행렬, 모험가의 시작 좌표는 1, 1
# 참고 : 시뮬레이션 유형 - 제시하는 요구사항에 따라 단계별로 수행
n = int(input("공간의 크기 : "))
m = input("이동 : ").split()
x,y = 1,1
for i in m:
    if i.upper() == "U":
        if x > 1:
            x -= 1
    elif i.upper() == "D":
        if x < n:
            x += 1
    elif i.upper() == "L":
        if y > 1:
            y -= 1
    elif i.upper() == "R":
        if y < n:
            y += 1
    else:
        continue
print(x,y)

n = int(input('NxN 2차원 행렬을 생성(N 입력): ')) # 2차원 행렬 입력
plans = input('L, R, U, D 4가지 방향 이동 계획 입력 : ').split() # 이동 계획 입력
x, y = 1, 1 # 초기 사용자의 좌표 위치

dx = [0, 0, -1, 1] # X축 방향은 행
dy = [1, -1, 0, 0] # Y축 방향은 열
move_types = ['R', 'L', 'U', 'D'] # 계획서 이동 타입 정의

for plan in plans:
    for i in range(len(move_types)): # 입력한 이동 타입 개수 만큼
        if plan == move_types[i]: 
            nx = x + dx[i] # 0이고
            ny = y + dy[i] # 1이면 다음위치 : 예) 동쪽으로 이동
            
    if nx < 1 or ny < 1 or nx > n or ny > n: # 공간을 벗어나는 경우 무시
        continue
        
    x, y = nx, ny # 공간이 벗어나지 않으면 이동

print('모험가 최종 좌표 :', x, y) # 모험가의 최종 좌표 출력
