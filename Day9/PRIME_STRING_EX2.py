# 문제 : 숫자로 이루어진 문자열이 주어진다. 부분 문자열 중에서 가장 큰 소수를 찾는 프로그램을 작성하시오.
# 참고 : 2 <= 100,000 이하 범위 소수만 소수이다. 
# 참고 : 입력은 여러 개의 테스트 케이스로 이루어짐, 1000개 이하
# 참고 : 각 테스트는 길이 255 이하 문자열로 구성, 마지막 줄 0 입력하면 종료
# 요구사항 : 시간 제한 1초, 메모리 128MB

# 입력			출력
# 11245			  11
# 91321150448	  1321
# 1226406		  2
# 0			      종료

# 문제 해결을 위한 아이디어? 소수 판별 및 에라토스테네스 체를 활용한다. 
# 문자열 안에 소수가 존재(in)하는지 검사(캐스팅)하고 최대값(max)을 출력한다. 
import time
import os
import psutil
import math

while True:
    n = int(input())
    
    process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
    start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가
    
    if n == 0:
        break
        
    array = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
                
    max_prime = 0
    for i in range(2, n + 1):
        if array[i]:
            if str(i) in str(n):
                if i > max_prime:
                    max_prime = int(i)
            
    print(max_prime)
    end_time = time.time() # 측정 종료
    print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
    print("MB bytes :", process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력
            
