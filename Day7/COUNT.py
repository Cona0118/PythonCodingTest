# 계수 정렬 : 최댓값 K를 입력 배열의 원소 값 개수 N을 누적합으로 구성한 배열로 정렬을 수행
# 데이터를 하나씩 모두 확인 후 검증 리스트를 생성
# 인덱스 데이터 1 증가

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

# 계수 정렬 예) 점수가 낮은 학생부터 이름 출력하기
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0],int(input_data[1]))) 
    array = sorted(array, key=lambda student: student[1]) # 람다식, 키 기준 정렬
    
    for student in array:
    	print(student[0], end=' ')
