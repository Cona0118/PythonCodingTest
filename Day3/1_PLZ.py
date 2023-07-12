# 문제 : N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택 수행하는 방법은? 최소값을 출력하시오.
# 참고 : 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 참고 : N에서 1을 뺀 후, N을 K로 나눈다. 

import time
import os
import psutil
process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

# n, k = map(int, input('두 수를 공백으로 분리하여 입력 : ').split()) # N, K을 공백을 기준으로 구분하여 입력 받기
n = 104195125111234124
k = 4
counter = 0
while n != 1:
    if n % k == 0:
        n = n/k
    else:
        n = n-1
    counter += 1
print(counter)        
            
end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print("MB bytes :", process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력