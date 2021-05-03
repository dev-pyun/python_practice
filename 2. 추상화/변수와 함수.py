#변수의 지정 : 지정 연산자 '='을 이용한다.

def hello() :
    print("Hello!")
    print("Welcome to Codeit!")
#다른언어에서는 {중괄호}로 함수 정의의 길이를 지정

print("함수 호출 전")
hello()
print("함수 호출 후")

'''
함수의 호출 순서 : 기본적으로 위에서 아래로 향한다!
'''

def square(x):
    return x ** 2  #return은 띄어쓰기만 하면 괄호 안붙여도 ok! return 없으면 none으로 나옴!

print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")

