상수 (constant) -> 상수는 대문자로 쓰는게 규칙임.
PI = 3.14   #절대로 바꾸지 않겠다는 약속임.
radius = 5

# def circle(radius, width = radius * radius * PI) :
'''위에처럼 선언하면 width에 optional parameter가 선언되어
    항상 width = radius * radius * PI 꼴로 입력해야함.
'''

#Sol
def circle(radius) :
    print(f"반지름이 {radius}면 넓이는 {radius*radius*PI}")

# PI = 3.14
#
# def calculate_circle(r):
#     x = PI *  r * r
#     return(x) # x값을 함수 호출부에 반환
#     # return 값을 안씀.
#
# radius = 4
# print("반지름이 {}이면 넓이는 {}이다.".format(radius, calculate_circle(radius)))
