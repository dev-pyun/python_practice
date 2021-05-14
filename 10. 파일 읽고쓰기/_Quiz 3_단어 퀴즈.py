with open('vocabulary.txt', 'r', encoding='utf-8') as d:
    voca = {}
    for i in d:
        temp_list = i.strip().split(': ')
        voca[temp_list[1]] = temp_list[0]

    correct_num = 0

    for key, value in voca.items():     #dictionary에서 다 불러오려면 items 써야된다..
        answer = input(f"{key}: ")
        if answer == value:
            print('맞았습니다!')
            correct_num += 1
        else:
            print(f'아쉽습니다. 정답은 {value}입니다.')
        print()

    print(f"맞춘 단어 수 : {correct_num} / {len(voca)}")


#굳이 for문을 두번 쓰지 않고도 푸는 방법
'''
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        
        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))
        
        # 정답 확인하기
        if guess == english_word:
            print("정답입니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
'''