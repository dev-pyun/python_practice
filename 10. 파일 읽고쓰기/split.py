# split : 문자열을 쪼개서 리스트화 함
# split() : 띄어쓰기 하나를 기준으로 잘라서 리스트화함.

full_name = 'Kim, Yuna'.split(", ")

#패턴이 안보이는 문자열을 쪼개기
list = "     \n\n   2   \t 3   \n   5 7 11  \n\n".split()

print(int(list[0]) + int(list[1]))

# 만약 \을 기준으로 split을 하고 싶다면 \\을 적으면 됨!
# list comprehension을 이용해 반복적인 방식으로 새 리스트를 만들 때 간편하게 할 수 있음.
# new_list = [원하는 return 식 for x in old_list]