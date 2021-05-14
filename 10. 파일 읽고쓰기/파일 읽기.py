'''
파일 불러오는 법
with open('열 파일', 'r') as f:
    open 함수로 파일을 열 수 있다!
    r은 read의 약자임. 파일에 쓰고 싶을 때는 w를 쓰면됨.
    같은 폴더안에 열 파일이 없으면 파일 위치도 지정해 줘야함.
    
    f는 for문을 이용해서 list와 비슷하게 출력 가능
'''

with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for i in f:
        print(i.strip())



