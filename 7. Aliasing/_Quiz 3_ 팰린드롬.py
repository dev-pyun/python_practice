#팰린드롬이 맞는지 아닌지를 확인하는 프로그램을 제작하시오.

def is_palindrome(word):
    temp_list = list(word)
    reverse_list = []
    for i in range(1, len(temp_list) + 1):
        reverse_list.append(temp_list[-i])

    return temp_list == reverse_list


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))