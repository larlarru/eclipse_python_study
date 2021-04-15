import random

mine = input("가위바위보를 선택하시오. :")

com ="";

# rnd = random.random()
rnd = random.randint(1,3)

if rnd == 1:
    com = "가위"
elif rnd == 2:
    com="바위"
elif rnd == 3:
    com = "보"
    
result = ""

if mine == com:
    result = "비겼습니다."
elif mine == "가위":
    if com == "바위":
        result = "졌습니다."
    elif com == "보":
        result = "이겼습니다."
elif mine == "바위":
    if com == "보":
        result = "졌습니다."
    elif com == "가위":
        result = "이겼습니다."
elif mine == "보":
    if com == "가위":
        result = "졌습니다."
    elif com == "바위":
        result = "이겼습니다."
print("rnd :",rnd)
print("mine :",mine)
print("com :",com)
print("결과 :",result)
    