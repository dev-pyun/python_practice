#2의 거듭제곱 찾는 문제
end = int(input("2의 몇제곱까지 알아보고 싶으세요?")) + 1

for i in range(end):
    print(f"2^{i} = {2 ** i}")
    print("2^{0} = {1}".format(i, 2 ** i))