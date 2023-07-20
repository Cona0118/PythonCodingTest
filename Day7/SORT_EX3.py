# 문제 : 코딩테스트 회원으로 가입한 사람의 나이와 이름은 순서대로 저장된다. 회원들의 나이순으로 정렬하는 출력하는 프로그램을 작성하시오.
# 참고 : 나이가 같으면 먼저 가입한 사람이 앞에 온다.

# 힌트 :정렬 함수의 람다식 사용, 키 기준 정렬

N = int(input("회원 수: "))
user = []
for i in range(N):
    user.append(list(input().split()))
    
sorted_user = sorted(user, key = lambda x : int(x[0]))
print("")
for i in sorted_user:
    print(i[0],i[1])