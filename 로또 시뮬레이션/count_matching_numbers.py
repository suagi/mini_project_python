from generate_numbers import generate_numbers as gen
from draw_winning_numbers import draw_winning_numbers as draw

def count_matching_numbers():
    my_num = gen(6)
    com_num = draw()
    count = 0

    for i in my_num:
        if i in com_num:
            count += 1
    return count

print(count_matching_numbers())