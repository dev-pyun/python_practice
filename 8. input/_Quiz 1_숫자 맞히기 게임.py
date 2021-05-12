from random import randint

correct = randint(1, 20)
trial = 1
max = 4


while trial <= max:
    choose = int(input(f"기회가 {max + 1 - trial}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if choose > correct:
        print("Up")
    elif choose < correct:
        print('Down')
    else:
        print(f"축하합니다. {trial}번 만에 숫자를 맞히셨습니다.")
        break
    trial += 1

if trial > max:
    print(f"아쉽습니다. 정답은 {correct}입니다.")


