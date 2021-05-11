alphabet_list = 'A B C D E F G H I J'.split()
print(alphabet_list)

alphabet_list = list('ABCDEFGHIJ')
print(alphabet_list)

#문자열에도 인덱스가 있고, 슬라이싱도 가능!
print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])

#list끼리 연결도 가능!
#문자열에서도 len()확인 가능!

# 문자열은 불변형 자료이므로 리스트와 달리 수정이 불가능

alphabet = 'ABCDE'
for hanguel in alphabet:
    print(hanguel)