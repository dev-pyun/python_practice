# #범위를 알아보자!
# #모든 변수에는 변수가 유효한 범위, 즉 scope가 존재한다.
# y = 5
# #여기서 y는 글로벌 변수임. 함수 밖에서 정의했으니! 변수x는 이 프로그램 전체에서 사용가능
# def my_function() :
#     x = 3
#     #여기서 x는 로컬 변수임. 이 함수 안에서만 사용가능.
#     #대표적인 예시는 파라미터가 있음음
#     print(x)
#
# my_function()
# print(x)
# print(y)

#함수에서 변수 사용시 로컬 변수 check 후 글로벌 변수 check

'''
    로컬 변수 : 변수를 정의한 함수 내에서만 사용가능
    글로벌 변수 : 변수를 정의한 프로그램의 어디든 사용가능
    함수에서 변수 사용시 로컬변수 찾은 뒤에 글로벌 변수 찾음.
    근데 이거 주석도 띄어쓰기 잘해야 된다...
'''
x = 2

def my(x) :
    x += 1
    #모양이 같더라도 로컬변수랑 지역변수는 다르다!
    #여기서 x += 1이 에러난 이유는 로컬변수x가 지정되지 않았는데 x + 1을 해서!
    #sol 1_ x앞에 global 붙여서 글로벌 변수임을 알려줌. global 선언시 함수 안에서도 함수 밖에서 정의한 변수 수정 가능
    #sol 2_ 파라미터에 미리 x의 자리를 만들어 놓기. -> x자리에 글로벌변수 집어넣으면 됨.
    print(x)
    return x


x = my(x)