# 배열 회전시키기

# 문제 설명
# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ numbers의 길이 ≤ 20
# direction은 "left" 와 "right" 둘 중 하나입니다.

# 입출력 예
# numbers	                direction	result
# [1, 2, 3]	                "right"	    [3, 1, 2]
# [4, 455, 6, 4, -1, 45, 6]	"left"	    [455, 6, 4, -1, 45, 6, 4]

def solution(numbers, direction):
    if direction == 'right':
        return numbers[-1:] + numbers[0:-1]
    else:
        return numbers[1:] + [numbers[0]]

# 다른 사람 풀이
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)