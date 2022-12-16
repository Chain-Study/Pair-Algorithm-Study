# https://school.programmers.co.kr/learn/courses/30/lessons/136797
# 예상 알고리즘: DP
# 베스트 알고리즘: DP, 그리디

def solution(numbers):
    weights = initWeight()
    numbers = list(map(int, list(numbers)))

    dp = {(4, 6): 0}
    for number in numbers:
        new_dp = {}
        for (idx1, idx2), total in dp.items():
            if idx1 == number or idx2 == number:
                result = min(new_dp.get((idx1, idx2), float('inf')), total + 1)
                new_dp[(idx1, idx2)] = result
            else:
                result1 = min(new_dp.get((idx1, number), float('inf')), total + weights[idx2][number])
                result2 = min(new_dp.get((number, idx2), float('inf')), total + weights[idx1][number])
                new_dp[(idx1, number)] = result1
                new_dp[(number, idx2)] = result2
        dp = new_dp
    return min(dp.values())

def initWeight():
    weight = [[0]*10 for _ in range(10)]
    keys = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9], 
            [-1, 0, -1]]
    # i에서 j까지 가는 가중치 비용
    all = [(i, j) for i in range(4) for j in range(3)] 
    for i, j in all:
        for k, l in all:
            if keys[i][j] == -1 or keys[k][l] == -1:
                continue
            weight[keys[i][j]][keys[k][l]] = 2*(abs(i - k) + abs(j - l)) - min(abs(i - k), abs(j - l))
            if keys[i][j] == keys[k][l]:
                weight[keys[i][j]][keys[k][l]] = 1
    return weight

print(solution("1756"))
print(solution("5123"))