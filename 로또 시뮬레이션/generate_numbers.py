import random

def generate_numbers(n):
    generate_list = []
    while len(generate_list) < n:
        select = random.randint(1, 45)
        if select not in generate_list:
            generate_list.append(select)

    return generate_list

print(generate_numbers(6))