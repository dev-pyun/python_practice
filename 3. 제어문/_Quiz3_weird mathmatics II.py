int = 1
sum = 0

while int < 1000:
    if (int % 2 == 0 or int % 3 == 0):
        sum = sum + int     #sum += int
    int += 1

print(sum)

#while 조건문의 비교연산자와 반복문 내에서의 += 사용에 아직 익숙치 않음.