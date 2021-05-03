'''
파라미터에 기본값을 설정할 수 있다. 이를 설정해 두면,
함수 호출시 꼭 파라미터에 값을 지정하지 않아도 됨.
이를 '옵셔널 파라미터'라고 함.
반드시 파라미터를 넘겨줄 필요가 없으니깐!
'''


def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우

'''옵셔널 파라미터는 모두 마지막에만 선언할 수 있음.
가령 
def myself(name, nationality="한국", age):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때
    로 설정하면 오류가 나옴
'''