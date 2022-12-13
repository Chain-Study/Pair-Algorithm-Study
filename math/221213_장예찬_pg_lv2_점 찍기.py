# https://school.programmers.co.kr/learn/courses/30/lessons/140107
# 예상 알고리즘: 탐색
# 베스트 알고리즘: 수학

# 솔루션
def solution(k, d):
    answer = 0
    for y in range(0, d+1, k):
        answer += (d**2 - y**2)**0.5 // k + 1
    return answer

print(solution(2, 4))