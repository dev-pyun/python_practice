from random import randint
import datetime

print(randint(1,10))

today = datetime.datetime.now()

print(today.strftime("%A, %B %dth %Y"))

# from datetime import datetime을 하게되면
# datetime안의 datetime 모듈만 가져오게 되는데,
# strptime은 클래스 안의 메소드이므로 import만으로는 호출안됨.

#그래서 strptime이 뭔데..?