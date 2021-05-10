#사전 속 자료 찾기
# values 메소드 사용
my_number = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

print(my_number.values())
for value in my_number.values():   #my_number.values 안에 들어있는 녀석들을 순차적으로 불러옴.
    print(value)

print(my_number.keys())
for key in my_number.keys():       #my_number.keys 안에 들어있는 녀석들을 차례대로 불러옴
    print(key, my_number[key])

for key, value in my_number.items():
    print(key, value)