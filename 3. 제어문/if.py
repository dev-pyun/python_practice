'''
조건문 형식
if 조건부분 : (얘가 true이면)
    실행부분  (실행부분 실행)
'''

#else는 형식적으로 사용하는 것이다.

temperature = 16

if (temperature <= 10) :
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다.")

#elif 드가자~
#다양한 케이스가 있을 때 물론 if else만 써도 okay지만..

#if~ elif~ elif~ 구조와 if~ if~ if~ 구조의 차이는 elif는 true 만족시 탈출한다는 점에서 차이가 있다.
