'''
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.

A를 3만큼 밀면 D가 되고 z를 1만큼 밀면 a가 됩니다. 공백은 수정하지 않습니다.

보낼 문자열 s와 얼마나 밀지 알려주는 n을 입력받아 암호문을 만드는 ceasar 함수를 완성해 보세요.

“a B z”,4를 입력받았다면 “e F d”를 리턴합니다.
'''

def caesar(s, n):
    n = n%26
    result_list_number = []
    result_list_string = []
    for i in range(len(s)):
        result_list_number += [ord(s[i]) + n]
        if ord(s[i]) > 90-n and ord(s[i]) < 91:
            result_list_number[i] -= 26
        if ord(s[i]) > 122-n and ord(s[i]) < 123:
            result_list_number[i] -= 26
        if ord(s[i]) == 32:
            result_list_number[i] -= n

        result_list_string += [chr(result_list_number[i])]
        result = ''.join(result_list_string)

    return result


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
