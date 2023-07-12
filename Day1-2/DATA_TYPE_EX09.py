# 문제 : 국어, 수학, 영어, 도덕, 물리 5개 과목의 데이터를 dic_sum 사전으로 생성하고, 전체 평균 점수를 구하시오.
# 점수는 직접 입력한다. (전체 점수 / 과목 개수)
dic_sum = {"국어":90, "수학":84, "영어":83, "도덕":74, "물리":68}

score_list = dic_sum.values()
score_sum = 0
for i in score_list:
    score_sum += i
print("평균점수 :",score_sum/len(dic_sum))