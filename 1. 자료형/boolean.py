# boolean 쓸거면 문자열("") 안에 T/F 삽입하지 않는게 좋아용

A = True
B = False

#ctrl + shift + 좌우 방향키 => 그 방향에 있는 단어를 모두 칠함
#마우스 드래그 후 "이나 ' 누르면 알아서 드래그 된 부분 감싸줌

print(A and A)
print(A and B)
print(B and A)
print(B and B)

print(A or A)
print(A or B)
print(B or A)
print(B or B)

print(not A)
print(not B)

#어케 쓰는지 알았으니 이제 명제에서 How 사용을 확인하자!
print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 3)
print(2 == 2)
print(2 != 2)

#문자열도 잘 사용할 수 있음당
x = input("정수를 입력해주세요")
x = int(x)

print(x > 4 or not (x < 2 or x ==3))