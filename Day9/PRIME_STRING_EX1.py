# 문제 : 예제 ALL_PRIME.py 의 공간 복잡도를 분석한다. 메모리 128메가 코딩테스트 문제의 기본적인 메모리 공간이다. 
#        공간 복잡도가 비교적 높다고 알려진 에라토스테네스 체의 공간 복잡도는?
# 요구사항 : 1만, 5만, 10만 범위까지 데이터를 확장해보자.

# 요구사항 : 시간 제한 1초, 메모리 128MB
# 문제 해결을 위한 아이디어? 기존 공간복잡도 소스 코드 활용

import time
import os
import psutil

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

import math

n = 100000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")



end_time = time.time() # 측정 종료
print()
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print("MB bytes :", process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력