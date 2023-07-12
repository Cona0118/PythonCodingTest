# 문제 : 사전의 데이터를 정렬/역정렬 하는 코드를 작성하시오. 사전 또는 집합은 순서가 없다. Sorted 함수를 활용한다.
# 키는 a, b, c, d, e 까지 값은 정수를 사용한다. (정의)

dic = {"a":1, "c":1, "d":1, "e":1, "b":1}
print(dic)

sorted_dic = sorted(dic.items())
print(sorted_dic)