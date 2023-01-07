# 문자열안에 문자열

# 문제 설명
# 문자열 str1, str2가 매개변수로 주어집니다.
# str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ str1의 길이 ≤ 100
# 1 ≤ str2의 길이 ≤ 100

# 입출력 예
# str1	                    str2	result
# "ab6CDE443fgh22iJKlmn1o"	"6CD"	1
# "ppprrrogrammers"	        "pppp"	2

def solution(str1, str2):
    return 1 if str2 in str1 else 2