from random import randint

def generate_numbers(n):
    correct_list = []
    for i in range(n):
        correct_list.append(randint(1, 45))
    return correct_list


def draw_winning_numbers():
    generate_numbers(n)


