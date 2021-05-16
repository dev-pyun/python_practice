from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        temp_num = randint(0, 9)
        if temp_num not in numbers:
            numbers.append(temp_num)  # randint는 파라미터 2개필요

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    i = 1
    while len(new_guess) < 3:
        # temp_num 이 숫자를 받는다는 가정하에 작성
        temp_num = int(input(f"{i}번째 숫자를 입력하세요 : "))
        if temp_num > 9 or temp_num < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        elif temp_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue

        new_guess.append(temp_num)
        i += 1

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(solution)):
        if guess[i] == solution[i]:
            strike_count += 1

        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    tries += 1
    guess_list = take_guess()
    s, b = get_score(guess_list, ANSWER)
    print(f"{s}S {b}B")

    if s == 3:
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
