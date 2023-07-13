# 문제 : 00시 00분 00초부터 정수 입력 N시 59분 59초까지의 모든 시각에서 3이 포함되는 모든 경우의 수를 구하시오.
# 참고 : 완전 탐색 유형  - 모든 가능한 경우의 수 구하기
import time
import os
import psutil

N = int(input("N시 : "))

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

counter = 0
for hour in range(N+1):
    for Min in range(60):
        for sec in range(60):
            if hour%10 == 3 or Min%10 == 3 or sec%10 == 3:
                counter += 1
            elif Min//10 == 3 or sec//10 == 3:
                counter += 1
            else:
                continue
print(counter)

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print("MB bytes :", process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력

print("----------------------------------")

# H 입력 받기
h = int(input('1시~23시 사이 시간 입력 : '))
process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가
count = 0
for i in range(h + 1): # 시간 
    for j in range(60): # 분
        for k in range(60): # 초
            if '3' in str(i) + str(j) + str(k): # 매 시각 안에 '3'이 하나라도 포함되어 있다면 참
                count += 1 # 카운트 증가
        #print(count)
print('최종 3이 카운트 된 결과는 :', count)

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print("MB bytes :", process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력
