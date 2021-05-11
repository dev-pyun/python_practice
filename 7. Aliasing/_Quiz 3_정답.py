# 문자열 자체에서도 len 함수와 index를 쓸 수 있기 때문에 굳이 list로 바꾸지 않아도 풀 수 있었음.
# list로 바꾸기 보다는 중심축을 기준으로 대칭되는지 여부만 확인하면 되니깐 for문 안에 if list[a] != list[b] 라고하면 되었다..

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))