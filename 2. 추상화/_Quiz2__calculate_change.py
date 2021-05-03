def calculate_change(payment, cost):
    change = payment - cost
    cng_50000 = change // 50000
    cng_10000 = (change - 50000 * cng_50000) // 10000
    cng_5000 = (change - 50000 * cng_50000 - 10000 * cng_10000) // 5000
    cng_1000 = (change - 50000 * cng_50000 - 10000 * cng_10000 - 5000 * cng_5000) // 1000

    print(f"50000원 지폐: {cng_50000}장")
    print(f"10000원 지폐: {cng_10000}장")
    print(f"5000원 지폐: {cng_5000}장")
    print(f"1000원 지폐: {cng_1000}장")
#파이썬에서는 indent(들여쓰기)가 중요해!


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

#Sol.
#1_ 우선 문제해결을 어떻게 해야할지부터 생각! coding은 그저 명령이다.
#2_ 어떻게 코드를 짤지 생각했다면, 어떻게 코드를 표현할지 생각.
# 본 문제에서는 //연산자와 %연산자를 이용해 몇장의 지폐와 남은 금액 표시함.
#3_ 어떻게 코드를 더 줄일 수 있을지, 명료하게 할 수 있을지 생각.
# 본 문제에서는 나머지를 구할 때 % 쓴 것과 더 명쾌하게 50000이 10000의 배수임을 이용한 것이 있음.
def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)