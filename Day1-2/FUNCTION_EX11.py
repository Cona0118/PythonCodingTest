# 문제 : 입력으로 들어오는 모든 수의 평균값 계산하는 함수 작성하기
# 입력 개수는 가변이다. 함수 이름 : avg
# 리스트 활용, for문, append로 데이터 저장
# 전체 합  / len 함수 = 평균을 리턴
def avg(*args):
    lst = []
    for i in args:
        lst.append(i)
    return(sum(lst)/len(lst))
    
print(avg(10,20,30))