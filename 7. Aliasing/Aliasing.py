#어떤 녀석이 alias인지 확인하는 것이 중요!

x = [2, 3, 5, 7, 11]
y = x
y[2] = 4

print(x)
print(y)

#오잉? 왜 x랑 y 모두 2,3,4,7,11로 출력되는거지?

'''
 변수로 선언한다는 것은 이름표를 붙이는 것과 같다.
 이때 한가지 이름표는 하나의 자료에만 붙일 수 있다.
 [2, 3, 5, 7, 11] 이라는 리스트에 x라는 이름표를 붙이고
 y = x
 를 통해 x라고 이미 이름표가 붙은 리스트에 다시 y라는 리스트를
 붙이게 되었다.
 그러므로 x랑 y는 같은 리스트를 지시하기 때문에 
 y를 통해 [2, 3, 5, 7, 11]이라는 리스트를 고치게 된 것이고, x는 같은 리스트를 지시하므로
 둘다 같은 값이 나옴.
 
 이때의 y는 alias(가명)이라고 함.
'''
y[2] = 5

y = list(x)     #이제 y는 x의 alias가 아님!
y[2] = 4

print(x)
print(y)