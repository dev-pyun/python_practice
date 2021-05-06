greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

count = 0

while count < 7:
    print(greetings[count])
    count += 1

#7 대신 len을 사용하면 더욱 안정적인 함수를 만들 수 있음!
#7이 greetings가 바뀜에 따라 알아서 바뀌게!
#더 좋은 방법은 len(greetings)를 아예 변수로 지정해서 더 빠르게 작동하도록!