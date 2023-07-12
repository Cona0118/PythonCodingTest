# 함수
def arugument(*args): # args는 매개변수 여러개 받음, *만 붙이면 됨
    a = 0
    for i in args:
        a = a + 1 # 인자 값 개수 증감
    return a

b = arugument(1, 2)
c = arugument(1, 2, 3, 4, 5)
d = arugument() # 인자 값이 없는 경우
print(b, c, d)
