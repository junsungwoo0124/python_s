# 컴퓨터가 생각하는 수를 맞추기
# 기회는 6번
#6번 이후에는 정답을 출력한다.

import random

a = random.randint(1,100)

for i in range(1,7):
    n = int(input("%d번째 예상숫자" % i))
    if a==n:
        print("정답")
        break
    elif a>n:
        print("더 큰수")

    else:
        print("더작은수")

if i == 6:
    print("아쉽네요, 정답은 %d 였습니다" % a)

