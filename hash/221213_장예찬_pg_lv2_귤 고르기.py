# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 예상 알고리즘: 딕셔너리
# 베스트 알고리즘: 딕셔너리(해시)

from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine = Counter(tangerine)
    for i, (_, count) in enumerate(tangerine.most_common(), 1):
        k -= count
        if k <= 0:
            answer = i
            break
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))