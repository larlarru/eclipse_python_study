import random

mine = input("홀/짝을 선택하시오...")


com ="";

rnd = random.random()
print(rnd)

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

result = ""
if mine == com:
    result = "이겼습니다."
else:
    result = "졌습니다."

print("내가 낸거 :",mine)
print("컴퓨터가 낸거 :", rnd)
print("결과 :", result)    
