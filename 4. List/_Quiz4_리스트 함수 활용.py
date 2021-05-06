# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
index = 0
while index < len(numbers):
    if numbers[index] % 2 != 0:
        del(numbers[index])     #여기에서 지워지면 index들이 한칸씩 앞으로 땡겨진다.. 그래서 7이 안지워졌던 것!
    else:
        index += 1

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20) #리스트.index(a,b) a앞자리에 b를 대입하세요 라는 의미!
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)


'''
중간에 if.. else 부분을 더 깔끔하게 바꿀 수 있는 방법:
index 호출법에는 -를 이용해 오른쪽부터 호출하는 방법이 있다!
'''