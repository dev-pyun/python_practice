from math import pi as PI

change_list = [['rad/s', 'rpm', 30/PI],[]]      #리스트에 [단위1, 단위2, 단위1을 2로 바꿔주는 상수]순으로 작성

while True:
    mode = int(input('''
    ===========================================
    변환할 단위를 선택하세요
    1. rad/s <-> rpm
    2. 추가예정
    3. 프로그램 종료
    ===========================================
    '''))

    if mode == len(change_list):
        break

    front = change_list[mode-1][0]
    back = change_list[mode-1][1]
    switch = input(f'1.{front} -> {back}? or 2. {back} -> {front}?')
    value = int(input('계산하고자 하는 값을 입력해주세요'))