# 문제 : 정수 3개 입력 받아 합과 평균 출력하시오.
# map(int, input().split()) 활용, 또는 3개 정수 캐스팅
a,b,c = map(int, input("정수 3개 입력: ").split())
total = a+b+c
print(total, format(total/3,".3f"))