'''
어떤 수 N(1≤N≤1,000,000) 이 주어졌을 때, N의 다음 큰 숫자는 다음과 같습니다.

N의 다음 큰 숫자는 N을 2진수로 바꾸었을 때의 1의 개수와 같은 개수로 이루어진 수입니다.
1번째 조건을 만족하는 숫자들 중 N보다 큰 수 중에서 가장 작은 숫자를 찾아야 합니다.
예를 들어, 78을 2진수로 바꾸면 1001110 이며, 78의 다음 큰 숫자는 83으로 2진수는 1010011 입니다.
N이 주어질 때, N의 다음 큰 숫자를 찾는 nextBigNumber 함수를 완성하세요.
'''

import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

def dec_to_bin(x):
    return int(bin(x)[2:])

def bin_to_dec(x):
    return int(str(x), 2)


def nextBigNumber(n):
    n_2 = dec_to_bin(n)
    count = list(str(n_2))
    count.insert(0, '0')
    answer = 0
    a = 0

    for i in range(len(count)-1, 1, -1):
        if count[i] == '1' and count[i-1] == '0':
            count[i] = '0'
            count[i-1] = '1'
            count[i:] = sorted(count[i:])
            break

    count.pop(0)
    answer = ''.join(count)

    return bin_to_dec(int(answer))

#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))
