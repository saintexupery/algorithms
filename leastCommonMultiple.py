def gcd(a,b):
    while(b != 0):
        temp = a % b
        a = b
        b = temp

    return abs(a)

def lcm(a,b):
    return a * b / gcd(a,b)

def nlcm(num):
    answer = 0

    if len(num) == 1:
        return num[0]

    a = num.pop()
    b = num.pop()
    answer = lcm(a,b)

    while(len(num) != 0):
        answer = lcm(answer, num.pop())

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));
