with open("data/chicken.txt", 'r', encoding= 'utf-8') as d:
    money_list = []
    for i in d:
        temp = i.strip()
        temp_list = temp.split(': ')
        money_list.append(temp_list[1])

    sum = 0
    for n in range(len(money_list)):
        sum += int(money_list[n])

    print(sum / len(money_list))

#모범답안
'''
with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ") #바로 일시적인 리스트 생성
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)
'''