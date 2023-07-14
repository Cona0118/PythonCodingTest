# 문제 : 왕실정원 체스판 8 X 8 2차원 행렬로 구성된다. 특정 위치에서 함정을 회피하고 나이트가 이동할 수 있는 경우의 수를 출력하라.
# 참고 : 나이트는 L자 형태만 이동가능(2가지 경우로 이동 가능)
# 참고 : 행 1~8, 열 a~h로 표현

# 참고 : 기존 왕실의 나이트 예제와 동일
# 조건 추가 : 체스판 8X8의 64개 좌표 내에 6개의 함정이 설치됬다. 이동 불가
# 함정 6개 설치 위치는 실행마다 랜덤

# 입력 : c2  
# 출력 : 5번 이동할 수 있습니다. (함정 1회 회피!)

import random

dx = ["a","b","c","d","e","f","g","h"]
place = list(input("나이트의 위치: ").lower()) # 나이트의 위치 입력받아 리스트화 ["a", "2"]
step = [ (2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2) ]

knight_x = dx.index(place[0])+1 # 나이트 위치 x값 정수화 a = 1
knight_y = int(place[1]) # 2

bomblist=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for a in range(6):
    bx = random.randint(1,8)
    by = random.randint(1,8)
    while [bx,by] in bomblist: # 기존의 함정 위치와 동일하면 재설정
        bx = random.randint(1,8)
        by = random.randint(1,8)
    bomblist[a][0] = bx
    bomblist[a][1] = by

counter = 0
bomb_counter= 0
for i in range(8):
    if 0 < knight_x + step[i][0] < 9: # 나이트의 이동 후 체스 판 밖으로 나가지면 제외
        if 0 < knight_y + step[i][1] < 9:
            if [knight_x + step[i][0],knight_y + step[i][1]] not in bomblist: # 이동 후 위치가 폭탄의 위치가 아니면
                counter += 1 # counter 증가
            else:
                bomb_counter += 1 # 폭탄의 위치면 bomb_counter 증가
        
            
print("나이트의 이동가능 위치의 수:",counter)
print("함정에 막힌 나이트의 이동가능 위치의 수:",bomb_counter)

