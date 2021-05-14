from random import randint

with open('vocabulary.txt', 'r', encoding='utf-8') as voca:
    dict_eng = {}
    dict_kor = {}
    i = 0
    for vocb in voca:
        temp_list = vocb.strip().split(': ')
        dict_eng[i] = temp_list[0]
        dict_kor[i] = temp_list[1]
        i += 1

    trial = 1
    correct = 0
    while True:
        index = randint(0, len(dict_kor) - 1)
        answer = input(f"{dict_kor[index]}: ")

        #종료여부 판정
        if answer == 'q':
            correct_rate = correct / trial * 100
            print(f'프로그램을 종료합니다. 정답률은{round(correct_rate, 1)}% 입니다.')   #round가 소수 자리수 조절이다..
            break

        #정답여부 판정
        if answer == dict_eng[index]:
            print("맞았습니다!")
            correct += 1
        elif answer != dict_eng[index] and answer != 'q':
            print(f"아쉽습니다. 정답은{dict_eng[index]}입니다.")


        trial += 1