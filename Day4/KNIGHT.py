# 문제 : 왕실정원 체스판 8 X 8 2차원 행렬로 구성된다. 특정 위치에서 고장난 나이트가 이동할 수 있는 경우의 수를 출력하라.
# 참고 : 나이트는 L자 형태만 이동가능(2가지 경우로 이동 가능)
# 참고 : 행 1~8, 열 a~h로 표현
dx = ["a","b","c","d","e","f","g","h"]
place = list(input("나이트의 위치: ").lower())
step = [ (2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2) ]

knight_x = dx.index(place[0])+1
knight_y = int(place[1])

counter = 0
knight_way =[]

for i in range(8):
    if 0 < knight_x + step[i][0] < 9:
        if 0 < knight_y + step[i][1] < 9:
            counter += 1
            knight_dx = dx[knight_x + step[i][0]-1]
            knight_way.append( knight_dx + str(knight_y + step[i][1]) )
print("나이트의 이동가능 위치:",counter)
knight_way.sort()
print(knight_way)

print("--------------------------------------------------------------------------------------------------------------")

input_data = input('나이트의 위치 a~h, 1~8 입력 하기 : ') # 현재 나이트의 위치 입력받기, a1
row = int(input_data[1]) # 정수형 입력 받음, 1
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 아스키 코드로 변환, 인덱스 값 계산을 위해 a를 뺀다. 이후 더하기 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 시뮬레이션 문제와 같이 좌표 이동 정의
result = 0 # 이동 횟수 초기화

for step in steps: # steps 8가지 방향을 순서대로 수행
    next_row = row + step[0] #  steps 요소 더하기
    next_column = column + step[1] # steps 요소 더하기
    print(next_row, next_column) # 내부 좌표 디버깅
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8: # 둘다 1이상 8이하이면
        result += 1 # 해당 위치로 이동이 가능하다면 카운트 증가
        
print(result)
