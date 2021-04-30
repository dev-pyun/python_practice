from math import pi as PI

change_list = [['rad/s', 'rpm', 30/PI],[]]      #리스트에 [단위1, 단위2, 단위1을 2로 바꿔주는 상수]순으로 작성

mode = int(input('''
===========================================
변환할 단위를 선택하세요
1. rad/s <-> rpm
2. 추가예정
3. 프로그램 종료
===========================================
'''))

front = change_list[mode-1][0]
back = change_list[mode-1][1]
CONST = change_list[mode-1][2]
value = int(input('계산하고자 하는 값을 입력해주세요'))

while True:
    switch = input(f'1.{front} -> {back}? or 2. {back} -> {front}?')
    if switch == '1':
        print(f'{round(value * CONST,4)}{back}입니다.')
    elif switch == '2':
        print(f'{round(value / CONST,4)}{front}입니다.')
    else:
        print('둘중에 하나만 고르세요')
        continue

    break
