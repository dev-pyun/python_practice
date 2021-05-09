#while 과 for 사이 차이?

'''
for문은 리스트의 내역을 반복할 시에 좋음

my_list = [2, 3, 5, 7, 11]

for numbers in my_list:
    print(numbers)

    여기서 numbers는 다르게 지정되어도 괜춘해!
'''

#for 반복문을 이용해서 1~10까지 출력하는 프로그램 제작해보자.
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    pass
#근데.. 1~ 100이면? 1000이면? 귀찮슴다..
#Sol. range 함수 : 리스트 슬라이싱이랑 비슷혀!
#장점 : 간편, 깔끔, 메모리 효율성

#파라미터 1개
for i in range(10):      #0부터 9까지 출력
    print(i)

print("")

#파라미터 2개
for i in range(2, 10):       #2부터 9까지 출력
    print(i)

print("")

#파라미터 3개
for i in range(1, 10, 3):        #1부터 9까지 3의 간격으로 출력
    print(i)