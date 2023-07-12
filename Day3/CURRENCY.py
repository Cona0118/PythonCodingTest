import time
import os
import psutil

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

n = 1260 # n = int(input("거스름돈을 가격(정수)로 입력해 주세요 :")) # 가격 입력을 받기 위해 정수 캐스팅
count = 0

array = [500, 100, 50, 10] # 큰 단위의 화폐부터 차례대로 확인하기
for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print('동전의 거스름돈 최소 개수는 :', count) # 개수 결과 출력

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print("MB bytes :", process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력
