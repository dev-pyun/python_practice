#텍스트 파일을 출력할 때 한줄이 아예 들여쓰기 되는 경우 존재.
#이는 텍스트 파일에서 Enter을 치면 \n으로 인식하기 때문!
#How 붙여쓰기 가능?

#strip을 사용하면 space, tab, enter 등의 화이트 스페이스 제거 가능
print("     abc     def     ".strip())

#중간의 공백 제거는 strip으로 불가, but replace를 이용하면 간접적으로 가능.
#혹은 마지막부분만 제거하고 싶으면 end='' 쓰면 ok!

with open("data/chicken.txt", 'r', encoding ='utf-8') as s:
    for line in s:
        print(line,end='')


#as 뒷부분은 f: 대신 s: 등등 ':'만 붙으면 뭐든지 가는ㅇ!