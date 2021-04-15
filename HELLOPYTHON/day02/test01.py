# 수학 점수를 입력하시오
# 국어 점수를 입력하시오
# 영어 점수를 입력하시오
# 평균
# 총점

math = input("수학 점수 입력 :")
kor = input("국어 점수 입력 :")
eng = input("영어 점수 입력 :")

sum = int(math) + int(kor) + int(eng)

avg = sum/3

print("수학 :",math)
print("국어 :",kor)
print("영어 :",eng)
print("평균 :",avg)
print("총점 :",sum)