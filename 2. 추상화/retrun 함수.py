#return은 (함수가)함수 호출부에 어떤 값을 돌려준다! return으로 함수 부분 대체됨

#함수를 즉시 종료시키는 역할도 있음!
#예제
def square(x):
    print("함수 시작")
    return x ** 2
    print("함수 끝")

print(square(3))
print("Hello world!")

'''
이때, return으로 인해 함수가 종료되므로 8번줄은 아무 의미가 없음
And that is Dead Code.
'''

#print와 return의 차이

def print_square(x) :
    print(3 ** 2)

def get_square(x) :
    return x ** 2

print_square(3) #함수내에서 3제곱 실행되어 9 출력
print(get_square(3)) # 3의 제곱이 계산되어 get_square이라는 함수 자체를 대체함

print(print_square(3))
#print_square은 값을 프린트 하라는 것이었으니 9를 일단 출력
# 그런데 return이 없으므로 print_square이 끝나면 none을 돌려받음.
# 그래서 None이 프린트 됨.
#파이썬은 return이 정의되지 않은 함수는 함수 호출부에 None을 반환하게 되어있음
#함수 호출이란 함수이름 뒤에 ()이 있는 경우를 말함.

# print(type(print_square()))  #Nonetype 출력
# print(type(print_square))    #변수에 함수를 선언하고 싶다면 함수 뒤의 (parameter)부분은 빼줘!
# print(type(print))