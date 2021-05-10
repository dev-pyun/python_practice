#사전 (dictionary)
# key - value pair (키-값 쌍)
my_dictionary = {5: 25, 2: 4}
# 여러줄 걸쳐서 작성도 가능함.

print(type(my_dictionary))
print(my_dictionary[2])

# .keys 메소드를 쓰면 key값들 출력가능
# 딕셔너리 안에 리스트를 넣을 수도 있다!

my_dictionary[5] = 25
#dictionary[key] = value 꼴로 사전에 추가가능!

'''
list와 dictionary의 차이점

list는 무조건 index가 정수이고 순서대로 나오지만,
dictionary는 key가 굳이 정수일 필요도 없고, 순서대로 나올 필요도 없음.
'''