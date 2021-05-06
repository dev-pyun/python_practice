# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    global Celcius  # Celcius를 글로벌 변수로 선언.
    count = 0
    length = len(fahrenheit)
    Celcius = []

    while count < length:
        temp_F = fahrenheit[count]
        temp_C = (temp_F - 32) * 5 / 9
        temp_C = round(temp_C, 1)
        Celcius.append(temp_C)
        count += 1

    fahrenheit = Celcius


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

temperature_list = Celcius
fahrenheit_to_celsius(temperature_list)
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력

#모범답안
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9    #def된 함수 호출하면 함수 실행 뒤 다시 return값 호출
#return으로 함수 호출부에 값을 돌려줄 생각을 했어야!

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1
print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력