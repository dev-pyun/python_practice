MONEY = 50000000
year = 1
BEFORE = 1988
now = 2016
EUNMA_NOW = 1100000000


while year <= now - BEFORE:
    MONEY *= 1.12
    year += 1

MONEY = int(MONEY)

if MONEY > EUNMA_NOW:
    print(f"{MONEY - EUNMA_NOW}원 차이로 동일 아저씨 말씀이 맞습니다.")
elif MONEY < EUNMA_NOW:
    print(f"{EUNMA_NOW - MONEY}원 차이로 미란 아주머니 말씀이 맞습니다.")


""" 모범답안
# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:  #year 값을 따로 지정 X한 점 굿!
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))
"""


'''
round(N, 1)이라고 하셨느데 자연수로 만들거면 뒤에 아무값도 안넣어도 됩니다. 2번째 파라미터로 1을 넣으면 소숫점1자리까지 표기하게 됩니다.

round는 계산해서 값을 return하는 함수입니다. 그래서 N이라는 변수의 값을 반올림 처리할 때 round(N)만 한다고 되는게 아니라 N = round(N)이 되어야 합니다.

그리고 print(f""+int{Dongil - 1100000000}+"원 차이로 동일 아저씨 말씀이 맞습니다.") 라고 하셨다고 했는데 이 방법 또한 int를 사용한거라고 볼 수 있습니다.

다만 문법적으로 int 뒤에 괄호가 {}로 되어있는데 int함수를 쓰려면 ()를 써야 합니다. f-string의 경우 {}로 변수를 중간에 삽입할 수 있지만 int() 의 경우 함수이기 때문에 ()를 써야 합니다.
'''