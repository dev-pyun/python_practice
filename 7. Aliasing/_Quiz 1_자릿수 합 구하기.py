def sum_digit(x):
    sum = 0
    x = str(x)              #x는 로컬 변수!
    for i in range(len(x)):     #len은 str에서만 사용가능!
        sum += int(x[i])

    return sum

everything = 0          #얘를 반복문 안에 넣으면 계속 0으로 나옴.
for i in range(1, 1001):
    everything += sum_digit(i)

print(everything)

#모범답안
# def sum_digit(num):
#     total = 0
#     str_num = str(num)
#
#     for digit in str_num:       #굳이 len으로 해서 index 지정 안해도 ok!
#         total += int(digit)
#
#     return total
#
#
# # sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# digit_total = 0
# for i in range(1, 1001):
#     digit_total += sum_digit(i)
#
# print(digit_total)