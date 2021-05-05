a = 1
b = 1
trial = 1

print(a)
print(b)

while trial <= 48:
    trial += 1
    c = a + b
    print(c)

    a = b
    b = c

''' 모범답안1
prvious = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1
'''

''' 모범답안 only in python
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1
'''