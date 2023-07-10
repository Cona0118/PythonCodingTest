# 문제 : 중첩된 반복문을 사용하여 구구단을 출력하자.
# For 문을 중첩, 2단부터 9단까지 출력, 출력 형식 : 2 X 1 = 2

for i in range(2,9+1):
    print("%d단" %i)
    for l in range(1,9+1):
        print("%d*%d=%d" %(i,l,i*l))
    print()