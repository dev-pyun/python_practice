# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000       #아니면 아예 환율 자체를 따로 지정해도 될 듯.
#함수 한번 정의하면 2줄 띄우기는 국롤 (PEP8)

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd * 125


# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

# amounts를 원화(￦)에서 달러($)로 변환하기
index = 0
while index < len(prices):  #len(prices) 쓰면 더 안정적으로 가능
    prices[index] = krw_to_usd(prices[index])
    index += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
index = 0
while index < len(prices):
    prices[index] = usd_to_jpy(prices[index])
    index += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))

'''
... 만약 한번에 원화에서 엔화로 환전하고 싶을 때
j = 0
while j < len(amounts):
  amounts[j] = usd_to_jpy(krw_to_usd(amounts[j]))
...'''

#새로운 리스트에 저장하고 싶다면,
#1 사용전에 미리 빈 리스트 필요
#2 빈 리스트에 .append() 방식으로 추가하는게 더 좋아용