def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1 # 부피는 0 이상이여야 함
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20) # 최대 크기 20
    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
     
while(1):
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        print(w(a,b,c))
