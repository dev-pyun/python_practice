#mission : for과 range를 사용해 numbers의 인덱스와 원소 출력

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# count = 0
#
# for i in numbers:
#     print(count, i)
#
#     count += 1


#모범답안
for i in range(len(numbers)):       #인덱스 목록 받아오기 0 ~ len(numbers) - 1 까지.
    print(i, numbers[i])

'''여기에서 i는 루프변수임! in 뒤에 오는 반복적 대상(여기서는 range)이
하나씩 루프변수에 할당되므로 미리 정의되지 않아도 ok!'''