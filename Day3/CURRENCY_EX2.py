# 문제 : N종류의 동전을 사용할 수 있다. 가격의 합 K를 만드는 동전 개수의 최소값을 출력하시오. 
# 참고 : 첫 째 줄에 N과, K가 주어진다. 
# 범위 : (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000) 
# 참고 : 둘째 줄부터 동전의 가치 Ai가 오름차순으로 주어진다. 
# 범위 : (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수) 큰동전은 작은 동전의 배수라는 의미이다.
# 요구사항 : 시간 제한 1초, 메모리 제한 256MB

import time
import os
import psutil

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

n = 10 # 동전 종류 수
k = 4200 # 거스름돈

coin_list = []
counter = 1
for i in range(1,n+1):
    if i == 1:
        coin_list.append(1)
    elif i == 2:
        coin_list.append(5)
    else:
        if i % 2 != 0:
            coin_list.append(50*counter)
        else :
            coin_list.append(100*counter)
            counter *= 10

coin_list = sorted(coin_list, reverse=True)
print(coin_list)
coin_counter = 0
for coin in coin_list:
    coin_counter += k // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    k %= coin
    
print('동전의 거스름돈 최소 개수는 :', coin_counter) # 개수 결과 출력
        
end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print("MB bytes :", process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력