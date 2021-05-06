numbers = []

print(len(numbers))     #list에 있는 변수들의 개수 알려줌
numbers.append(5)       #새로운 값을 리스트 오른쪽 끝에 추가
numbers.extend([6, 7, 8])       #요녀석들을 리스트 오른쪽 끝에 추가

num = [2, 3, 5, 7, 11, 13, 17, 19]
del num[3]              #3번 인덱스에 있는 녀석을 삭제하세요
num.insert(4, 27)       #4번 인덱스에 자리에 27을 삽입하세요

print(num)
print(numbers)

'''
같은 질문 같네용!!

Running help on method will usually give you the answer for these kind of questions:

help(list.insert)
#Help on method_descriptor:
#
#insert(self, index, object, /)
#    Insert object before index.
+ 추가)

help를 통해서 메소드의 기능을 기술해놓은 method_descriptor 를 확인할 수 있는데요!

Insert object before index
이에 따르면, list.insert  는 해당 index 위치 이전에 object를 삽입해요!'''

