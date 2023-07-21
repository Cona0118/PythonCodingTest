# 문제 : 최근 입원한 A씨는 알 수 없는 신종 코로나에 감염된 상태이다. 연결된 병동은 결국 모두 감염된다. 병동의 개수는?
# 참고 : A씨가 위치한 병동은 1동이다. 그림과 같이 병동의 연결에 따라 코로나가 전파될 수 있다. 
#     건물 내부 구조상 영향 받지 않는 방도 있다.

# 입력 예)
# 병동의 개수	: 7
# 연결된 병동의 수	: 6
# 1 2
# 2 3
# 1 5
# 5 3
# 5 6
# 4 7
# 감염됨 병동은 4개입니다.

n = int(input("병동의 개수: "))
connect = int(input("연결된 병동의 수: "))

connection = [] # 병동간 연결을 저장할 리스트
for i in range(connect):
    connection.append(list(map(int, input().split())))

infect = [1] # 감염된 병동을 저장할 리스트
infect_count = 0 
while infect_count != len(infect): # 추가로 감염된 병동이 없으면 종료
    infect_count = len(infect)
    for i in connection: 
        if any(x in i for x in infect): # 연결된 병동이 감염된 병동이면
            for j in i: # 다른 병동이
                if not j in infect: # 감염 병동 리스트에 없다면
                    infect.append(j) # 리스트에 추가한다
                    
print("감염된 병동은 %d개입니다." %(len(infect)-1)) # 최초 1 병동을 제외한 감염된 병동의 수 출력