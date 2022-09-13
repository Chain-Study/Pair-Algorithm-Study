# https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 예상 알고리즘: 1부터 n까지
# 베스트 알고리즘: 1부터 n까지

def solution(n):
    for i in range(1, n):
        if n%i == 1:
            return i

# print(solution(10))