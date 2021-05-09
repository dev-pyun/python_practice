numbers = [2, 3, 5, 7, 11, 13, 17, 19]

new_list = []

#range로 안감싸주면 'int' objective is not iterable이 나옴
for i in range(len(numbers)):
    new_list.insert(0, numbers[i])


print("뒤집어진 리스트: " + str(new_list))

''' #Sol
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1  
    
    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))'''

'''애초에 반복문 사용 X by sort
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

numbers.sort(reverse = True)

print("뒤집어진 리스트: {}".format(numbers))
'''