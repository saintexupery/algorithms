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
