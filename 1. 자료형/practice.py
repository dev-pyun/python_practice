print(type(print(3 > 1)))

# #파이썬의 출력순서는 괄호를 먼저 인식
# 따라서 3 > 1 이 먼저 인식되어 True 라는 값으로 바뀌고,
# 이후 print(True)이므로 True가 나옴
# 이때, return과는 다르게 print는 출력만 할 뿐, True를 돌려주지는 않으므로
# None이 돌아오게 되고, type(None)이 되어 이것이 다시 Nonetype이 되고,
# print(Nonetype)이 실행되면서 <class 'Nonetype'>이 출력된다.