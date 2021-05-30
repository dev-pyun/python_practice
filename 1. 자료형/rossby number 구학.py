from math import pi

a = 1
OMEGA = 7.2921 / (10 ** 5)
PI = pi

print(2*PI / OMEGA)

while True:
    a = input("초를 입력하시오")
    if not a:
        break

    a = int(a)
    print(2 * PI/(OMEGA * a))

