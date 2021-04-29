year = 2019
month = 10
day = 29

#format classmethod
'''
1. 우리가 쓰고 싶은 문장을 우선 작성한다.
2. 원하는 값을 넣어야하는 공간을 {}로 대체해준다.
'''

date_string = "오늘은 {}년 {}월 {}일 입니다."
#문자열을 계속 반복해서 사용할 것이면 선언을 미리 해주자.
print(date_string.format(year, month, day))
#그냥 그자리에 그대로 숫자를 대입할거면 굳이 중괄호에 번호 안적어도 괜춘해요
#.format의 괄호 안에서 연산을 해도 괜춘!

num_1 = 1
num_2 = 3
print("{0} 나누기 {1} 은 {2:}입니다.".format(num_1, num_2, num_1 / num_2))

'''소수 반올림 방법
1. round(n)하면 소수점 n자리까지 출력 
2. :.nf 사용 -> .n은 소수점 n번째자리까지 하기, f는 float라고 선언해주는 것
'''