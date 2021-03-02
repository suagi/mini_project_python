from random import randint

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print(numbers)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []

    while len(new_guess) < 3:
        A = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요: "))
        if A not in new_guess and 0 <= A < 10:
            new_guess.append(A)
        elif not 0 <= A < 10:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif A in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0

while True:
    S, B = get_score(ANSWER, take_guess())
    tries += 1
    if S == 3:
        print(f"{S}S {B}B")
        break
    else:
        print(f"{S}S {B}B")

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))