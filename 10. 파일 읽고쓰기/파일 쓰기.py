# new_file.txt를 쓰는 용도로 f 라는 변수에 저장하겠다.
with open('new_file.txt', 'w') as f:
    f.write("Hello world!") #f라는 변수로 저장된 new_file.txt에 Hello world! 삽입

#실행할 때마다 new_file에 추가하고싶다면? 'w'를 'a' (append)로 바꾸기!
# 'a'나 'w'나 불러오는 파일이 없는 파일이라면
