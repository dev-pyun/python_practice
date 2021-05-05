num = 1
count = 0
N = 120     #반복되어 사용되는 녀석은 쫌 제발 변수로 선언하자.

while num <= N:
    if N % num == 0:
        print(num)
        count += 1
    num += 1

print(f"120의 약수는 총 {count}개 입니다.")