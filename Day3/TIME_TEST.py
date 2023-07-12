import time
import random

start_time = time.time() # 측정 시작
array = [] # 리스트 생성

for v in range(10000): # N = 500인 경우는?
    array.append(random.randint(0, 10)) # 랜덤 값 추가
    
for i in array:
    for j in array:
        temp = i *  j
        print(temp) #- 반복마다 값 출력?
       
print(temp)# 측정 최종 값 출력
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
