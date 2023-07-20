from bisect import bisect_left, bisect_right

a = [1, 2, 3, 3, 3, 5, 10] 
x = 3

print(bisect_left(a, x)) # 왼쪽 인덱스 출력
print(bisect_right(a, x)) # 오른쪽 인덱스 출력

from bisect import bisect_left, bisect_right

def count_by_value(array, value):
    left_index = bisect_left(array, value)
    right_index = bisect_right(array, value)
    return right_index - left_index  # 특정 값의 개수 반환


array = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8]
# 특정 값을 입력받는다.
value = 3

# 특정 값의 개수를 세고 출력한다.
count = count_by_value(array, value)
print("특정 값의 개수는 {}입니다.".format(count))
