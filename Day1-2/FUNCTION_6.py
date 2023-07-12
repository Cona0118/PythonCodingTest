# 함수
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'black', 'red', 'red'])
print(counter['red']) # 'red'가 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 각 횟수 반환 출력

import math
def lcm(a, b): # 최소 공배수(LCM)를 구하는 함수
    return a * b // math.gcd(a,b)
a = 24
b = 36

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산
print(lcm(21, 14)) # 최소 공배수(LCM) 계산
