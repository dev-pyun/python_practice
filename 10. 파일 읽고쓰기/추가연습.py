revenue = {}

with open('data/chicken.txt', 'r', encoding='utf-8') as f:

    for line in f:
        data = line.strip().split('일: ')
        date = data[0]
        money = data[1]
        revenue[date] = money


    while True:
        dt = int(input("어떤 날짜의 매출이 궁금하신가요?"))
        print(revenue[dt])

        if date == 0:
            print("프로그램을 종료합니다.")
            break
