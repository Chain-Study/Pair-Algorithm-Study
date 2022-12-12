# https://school.programmers.co.kr/learn/courses/30/lessons/138475?language=python3
# 예상 알고리즘: 수학
# 베스트 알고리즘: 세그먼트 트리, 메모이제이션

# starts보다 크고 e보다 작은 수 중에서 약수의 개수가 가장 많은 수를 찾아라

def solution(e, starts):
    memo = [0] * (e + 1)
    
    # 각 원소는 해당 인덱스의 약수의 개수를 의미한다.
    # 모든 수를 1부터 e까지 순회하면서 해당 수의 약수의 개수를 하나씩 늘려가며 메모한다.

    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            memo[j] += 1
    maxNum = 0
    for i in range(e, 0, -1):
        if memo[i] >= maxNum:
            maxNum = memo[i]
            memo[i] = i
        else:
            memo[i] = memo[i + 1]
    
    return [memo[s] for s in starts]

print(solution(	8, [1, 3, 7]))