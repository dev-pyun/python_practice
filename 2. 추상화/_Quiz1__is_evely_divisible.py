# def is_evenly_divisible(number):  #여기 number는 로컬 변수임.
#     return not number % 2  #python에서는 0이 아닌 나머지값은 그냥 True
#
# #모범답안은  return number % 2 == 0 이다.
#
# print(is_evenly_divisible(3))
# print(is_evenly_divisible(7))
# print(is_evenly_divisible(8))
# print(is_evenly_divisible(218))
# print(is_evenly_divisible(317))


'''
return을 복수로 할 경우, 여러 반환 값들이 하나의 튜플 형태로 나타나게 됩니당!!

만약 출력과 같은 값을 반환하기를 바라신다면,

f-string을 이용하여서 str 값을 반환하는 것이 좋을 거 같아용!!

def is_evenly_divisible(number):
    calculation = number % 2
    return f'{calculation} 는 0과 같나요? {calculation == 0}'
'''

def is_evenly_divisible(number):
    calculation = number % 2
    return f'{calculation}는 0과 같나요? {calculation == 0}'


print(is_evenly_divisible(3))