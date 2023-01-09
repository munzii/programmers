# 가위 바위 보

# 문제 설명
# 가위는 2 바위는 0 보는 5로 표현합니다.
# 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < rsp의 길이 ≤ 100
# rsp와 길이가 같은 문자열을 return 합니다.
# rsp는 숫자 0, 2, 5로 이루어져 있습니다.

# 입출력 예
# rsp	result
# "2"	"0"
# "205"	"052"

def solution(rsp):
    x = ''
    for i in range(len(rsp)):
        if rsp[i] == '2':
            x += '0'
        elif rsp[i] == '0':
            x += '5'
        else:
            x += '2'
    return x

# 다른 사람 풀이
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp