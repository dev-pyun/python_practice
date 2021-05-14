with open('vocabulary.txt', 'a', encoding='utf-8') as dic:
    while True:
        English = input("영어 단어를 입력하세요: ")
        if English == 'q':
            break
        Korean = input("한국어 뜻을 입력하세요: ")
        if Korean == 'q':

            break
        dic.write(f'{English}: {Korean}\n')