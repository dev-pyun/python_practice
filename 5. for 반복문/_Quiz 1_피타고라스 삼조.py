'''
a < b < c라고 가정할 때,
a + b + c = 1000을 만족하는 피타고라스 삼조
(a, b, c)는 단 하나인데요.
이 경우, a * b * c는 얼마인가요?
'''
answer = True

for a in range(1, 999):
    for b in range(a + 1, 1000):        #a < b
        c = 1000 - (a + b)
        if b >= c or c <= 0:
            break

        if a ** 2 + b ** 2 == c ** 2:
            print(a * b * c)
            answer = False
            break

    if answer == False:
        break



# for a in range(1,10):
#     for b in range(a + 1, 10):
#         c = 10 - (a + b)
#         if c <= b or c <= 0:
#             break
#         else:
#             print(a,b,c)
#
