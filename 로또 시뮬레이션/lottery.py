import random

def generate_numbers(n):
    generate_list = []
    while len(generate_list) < n:
        select = random.randint(1, 45)
        if select not in generate_list:
            generate_list.append(select)

    return generate_list

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(my, com):
    count = 0

    for i in my:
        if i in com:
            count += 1

    return count

def check(my, com):
    result = count_matching_numbers(my, com[:6])
    bonus = count_matching_numbers(my, com[6:])

    if result == 6:
        return 1000000000
    elif result == 5 and bonus == 1:
        return 50000000
    elif result == 5:
        return 1000000
    elif result == 4:
        return 50000
    elif result == 3:
        return 5000
    else:
        return 0