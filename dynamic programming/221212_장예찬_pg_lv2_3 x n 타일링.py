# https://school.programmers.co.kr/learn/courses/30/lessons/12902
# 예상 알고리즘: DP
# 베스트 알고리즘: DP

def solution(n):   
    # 가로가 2이고 세로가 1인 직사각형 타일로 세로가 3이고 가로가 n인 직사각형을 채우는 방법의 수를 구하라.
    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11
    for i in range(5, n + 1):
        dp[i] = (dp[i - 2] * 4 % 1000000007 - dp[i - 4] % 1000000007) % 1000000007
    return dp[n]

print(solution(4))
print(solution(7))