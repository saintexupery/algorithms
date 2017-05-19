import math

def setAlign(n, k):
    answer = []
    align = [i for i in range(1, n+1)] # align = list(range(1,n+1))

    while n > 1:
        factorial = math.factorial(n-1)
        quotient = int(k / factorial) # quotient = k // factorial
        remainder = k % factorial

        if remainder == 0:
            answer.append(align.pop(quotient-1))

            while n > 1:
                answer.append(align.pop())
                n -= 1

        else:
            answer.append(align.pop(quotient))

            k = remainder
            n -= 1

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(setAlign(3, 5))
