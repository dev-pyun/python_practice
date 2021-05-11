#작대기 유무에 관계없이 마지막 네 숫자가 *로 교체되도록 하기.

def mask_security_number(security_number):
    temp_list = list(security_number)
    for i in range(1, 5):
        temp_list[-i] = '*'

    secured_num = ""
    for i in range(len(security_number)):
        secured_num += temp_list[i]

    return secured_num


#Sol 1
'''
def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str
'''

# Sol2. with join() method
# str.join(list)의 형태로 쓰임.
'''
def mask_security_number(security_number):
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = '*'

    # 리스트를 문자열로 복구하여 반환
    return ''.join(num_list)
    '''

#Sol3. 문자열 슬라이싱 이용
'''
def mask_security_number(security_number):
    return security_number[:-4] + '****'
    '''