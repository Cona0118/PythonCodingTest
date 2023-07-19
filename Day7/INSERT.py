# 삽입 정렬
array = [8, 5, 6, 2, 4]

for i in range(1, len(array)):  # 전체 루프
    print(i, "회전")
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            print("교환 전 : ", array[j - 1], array[i])
            array[j], array[j - 1] = array[j - 1], array[j]  # 자리 교환
            print("교환 후 : ", array[j - 1], array[i])
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array) 


