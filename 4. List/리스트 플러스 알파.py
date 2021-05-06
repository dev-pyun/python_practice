#1
# in을 이용하면 boolean을 통해 찾고자 하는 값이 있는지 아닌지 확인할 수 있어요!

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

print(13 in primes)
print(1 in primes)

print(13 not in primes)
print(1 not in primes)
print()

#2
#nested list : list 안에 또 리스트가 있지용
a = [62, 75, 77]
b = [78, 81, 86]
c = [85, 91, 89]
grades = []

grades.append(a)
grades.append(b)
grades.append(c)
print(grades)

#첫번째 학생의 성적
print(grades[0])

#두번째 학생의 둘째과목 성적
print(grades[1][1])

#세번째 시험의 평균
print((grades[0][2] + grades[1][2] + grades[2][2]) / len(grades)) #list는 ','로 묶여있기만 하면 하나의 item으로 취급!
print()

#3
#sort 메소드 & sorted 함수
some_list = [5, 3, 7, 1]

new_list = sorted(some_list)    #새로운 리스트에 정렬된 기존 리스트를 선언
some_list.sort()                #기존 리스트 자체를 새로 정렬시킴

print(new_list)
print(some_list)
print()

#4
#reverse 메소드 : some_list.reverse()는 some_list의 원소들을 뒤집어진 순서로 배치

numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)
print()

#5
#index 메소드 : some_list.index(x) 는 some_list에서 x값의 인덱스를 알려줌.
num = [1, 1, 1, 2, 2, 3]
print(num.index(1))     #여러개 중복될 경우 맨 앞의 인덱스로 알려줌.
print()

#6
#some_list.remove(x) : some_list에서 첫번째로 x 값을 가지는 원소를 삭제함.
fruits = ["딸기", "사과", "복숭아", "수박"]
fruits.remove("사과")
print(fruits)