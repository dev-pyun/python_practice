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


'''
continue 할 필요 없이 그냥 if elif 안에 전부다 넣었어도 괜춘
i를 굳이 새로 정의할 필요 없이 len + 1로 몇번째 시도인지 했어도 좋았을 듯.
range 함수 안에 0, 10 을 범위로 정해서 했어도 굿!
'''


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(solution)):
        if guess[i] == solution[i]:
            strike_count += 1

        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count
