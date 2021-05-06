# 리스트 (list)를 이용해 여러값을 변수하나에 저장할 수 있다!

numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]


#한꺼번에 여러개 가져올 수도!
print(numbers)
print(names)

#인덱싱 (indexing)으로 하나씩 가져올 수 있다!
#파이썬의 인덱싱은 왼쪽부터 0번부터 시작됨~!
print(numbers[1] + numbers[3])

#인덱스 범위를 벗어난 녀석을 호출하면 오류가 난다!

#-index 사용 가능! 얘는 오른쪽부터 -1, -2, -3... 요로코롬!

#리스트 슬라이싱 (list slicing)
print(numbers[0:4])     #numbers의 0번째 인덱스이상, 4번째 미만의 인덱스 출력.
print(numbers[2:])      #numbers의 2번째 인덱스 이상, 끝까지.
print(numbers[:3])      #numbers의 처음 인덱스부터 3번째 미만 인덱스 까지.

new_list = numbers[:3]  # [2,3,5]
print(new_list[:2])     # [2,3]

#리스트의 요소를 바꿔보자!
numbers[0] = 7      #0번 인덱스를 정수 7로 바꾸세요!
numbers[1] = numbers[1] + numbers[2]        #1번 인덱스를 1번 인덱스와 2번 인덱스의 합으로 바꾸세요!

print(numbers)
