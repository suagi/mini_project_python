from generate_numbers import generate_numbers as gen_num

def draw_winning_numbers():
    winning_numbers = gen_num(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

print(draw_winning_numbers())