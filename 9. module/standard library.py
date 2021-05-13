#standard library (표준 라이브러리)
#import는 웬만하면 코드 상단에 해주는게 좋음!
#여기서는 그저 예시를 위해 각각 따로 import 할 뿐임.
# 예시1. math
import math

print(math.log10(100))
print(math.cos(0))
print(math.pi)


#예시2. random
import random

print(random.random())      #0~1 사이의 float 아무거나 랜덤으로


#예시3. os _for 운영체제 조작
import os

print(os.getlogin())        #현재 접속한 아이디
print(os.getcwd())          #현재 파일의 위치