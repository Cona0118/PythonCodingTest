# 문제 : 무인도에 다수의 로봇이 NWES 중 하나의 방향을 향해 서 있다. 다음과 같은 명령 3가지를 순차적으로 실행하려 한다.
#        2가지 문제에 대한 안전성 검증을 위한 시뮬레이션 프로그램을 작성하시오.
# 참고 : 무인도 - 가로 A(1≤A≤100), 세로 B(1≤B≤100) 크기
# 참고 : 로봇의 개수 N(1≤N≤100)개, 초기 위치 X, Y(x좌표는 왼쪽부터, y좌표는 아래쪽)

# 명령 수행 3가지
#    L: 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전한다.
#    R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전한다.
#    F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.
# 잘못된 명령 2가지
#    Robot X crashes into the wall: X번 로봇이 벽에 충돌, 주어진 땅의 밖으로 벗어나는 경우
#    Robot X crashes into robot Y: X번 로봇이 움직이다가 Y번 로봇에 충돌하는 경우

# 입력 : 
# 첫째 줄에 두 정수 A, B가 주어진 후 두 정수 N, M이 주어진다.  5 4, 2 2
# 다음 N개의 줄에는 각 로봇의 초기 위치(x, y좌표 순) 및 방향이 주어진다. 1, 1, E 
# 다음 M개의 줄에는 각 명령이 명령을 내리는 순서대로 주어진다. 1, F, 7
#     의미 : 명령을 내리는 로봇 1, 명령의 종류 F, 명령의 반복 회수(1이상 100이하) 7

# 출력
# 문제가 없는 경우에는 OK 출력
# 그 외의 경우에는 잘못된 경우 2가지 명령을 중 하나를 출력(먼저 발생)하면 된다.
#     벽에 부딧침! 또는 로봇 충돌! 출력

# A , B = map(int, input("섬의 가로 세로 입력: ").split()) # 5 4
# N , M = map(int, input("로봇의 수와 지시할 명령의 횟수 입력: ").split()) # 2 2
A, B = 5, 4
N, M = 2, 2

robot_list = []
for i in range(N):
    print(i+1,end="")
    robot_list.append(input("번 로봇의 위치와 방향(NSEW) 입력: ").split())
    if robot_list[i][2].upper() == "N" :
        robot_list[i][2] = 0
    elif robot_list[i][2].upper() == "E" :
        robot_list[i][2] = 1
    elif robot_list[i][2].upper() == "S" :
        robot_list[i][2] = 2
    elif robot_list[i][2].upper() == "W" :
        robot_list[i][2] = 3

for i in range(len(robot_list)):
    robot_list[i] = list(map(int, robot_list[i]))

command = []
for i in range(M):
    dx , dy = 0 , 0
    command.append(input("로봇 번호, 명령, 반복횟수 입력: ").split())
    
    if command[i][1].upper() == "R":
        robot_list[int(command[i][0])-1][2] = (robot_list[int(command[i][0])-1][2] + 1 * int(command[i][2])) % 4 
        
    elif command[i][1].upper() == "L":
        robot_list[int(command[i][0])-1][2] = (robot_list[int(command[i][0])-1][2] + 3 * int(command[i][2])) % 4 
        
    elif command[i][1].upper() == "F":
        if robot_list[int(command[i][0])-1][2] == 0: # N
            dx = robot_list[int(command[i][0])-1][0]
            dy = robot_list[int(command[i][0])-1][1] + int(command[i][2])
        if robot_list[int(command[i][0])-1][2] == 1: # E
            dx = robot_list[int(command[i][0])-1][0] + int(command[i][2])
            dy = robot_list[int(command[i][0])-1][1]
        if robot_list[int(command[i][0])-1][2] == 2: # S
            dx = robot_list[int(command[i][0])-1][0]
            dy = robot_list[int(command[i][0])-1][1] - int(command[i][2])
        if robot_list[int(command[i][0])-1][2] == 3: # W 
            dx = robot_list[int(command[i][0])-1][0] - int(command[i][2])
            dy = robot_list[int(command[i][0])-1][1]
        
        if dx < 1 or dx > A:
            print(command[i][0],"번 로봇이 벽에 부딪혔다!")
        elif dy < 1 or dy > B:
            print(command[i][0],"번 로봇이 벽에 부딪혔다!")
        elif int(command[i][2]) != 0:
            for sublist in robot_list:
                if sublist[0] == dx and sublist[1] == dy:
                    print(command[i][0],"번 로봇이 다른 로봇과 부딪혔다!")
                    break
        else:
            robot_list[int(command[i][0])-1][0] = dx
            robot_list[int(command[i][0])-1][1] = dy 
            print(command[i][0],"번 로봇 이동 완료")

for i in range(N):
    if robot_list[i][2] == 0 :
        robot_list[i][2] = "N"
    elif robot_list[i][2] == 1 :
        robot_list[i][2] = "E"
    elif robot_list[i][2] == 2 :
        robot_list[i][2] = "S"
    elif robot_list[i][2] == 3 :
        robot_list[i][2] = "W"
            
print(robot_list)
