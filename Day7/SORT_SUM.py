# 문제 : N개의 자연수로 된 배열 A, B가 있다. 최대 K번의 원소 교환을 수행할 수 있다. 배열 A의 원소의 합의 최대값을 출력하는 프로그램을 작성하시오.
# 참고 : 원소 교환이란 두 배열의 원소 하나를 서로 바꾸는 것을 의미
# 범위 : 1 <= N <= 100,000, 0 <= K <= N, 배열 내부 원소는 10,000,000 이하 자연수

n,k =  map(int, input('n,k 입력 :').split())
Alist = list(map(int, input('A : ').split()))
Blist = list(map(int, input('B : ').split()))

Alist.sort()
Blist.sort(reverse = True)

for i in range(k):
    if Alist[i] < Blist[i]:
        Alist[i], Blist[i] = Blist[i], Alist[i]
    else:
        break

        
print(sum(Alist))


