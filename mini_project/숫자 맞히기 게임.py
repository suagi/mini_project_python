import random

# 코드를 작성하세요.
chance = 4
result = random.randint(1, 20)
print(result)

for i in range(chance):
    num = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(chance)))
    if result > num:
        chance -= 1
        print("Up")
    elif result < num:
        chance -= 1
        print("Down")
    elif result == num:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(i + 1))
        break

    if chance == 0:
        print("아쉽습니다. 정답은 {}입니다.".format(result))