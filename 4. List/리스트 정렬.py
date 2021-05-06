#어떻게 리스트의 요소를 바꾸고, 정렬할 수 있을까?

numbers = [19, 13, 2, 5, 3, 11, 7, 17]

num_list = sorted(numbers)  #오름차순으로 새로 정렬된 리스트를 생성
num_list = sorted(numbers, reverse = True) #내림차순으로 새로 정렬된 리스트 생성

numbers.sort()      #얘는 numbers 자체를 오름차순으로 정렬
numbers.sort(reverse = True)
#sort는 어떠한 값을 return해 주지는 않음!

print(numbers)
