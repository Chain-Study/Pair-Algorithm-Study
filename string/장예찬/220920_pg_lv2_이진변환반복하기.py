# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 예상 알고리즘: 문자열
# 베스트 알고리즘: 문자열

# 풀이 1
# def solution(s):          #제출 답변
#     count, zeroCount = 0, 0 #이진변환 / 빠진 0 의 개수
#     while len(s) != 1:
#         sNext = s.replace("0","") #아하
#         count += 1
#         zeroCount += len(s) - len(sNext)
#         s = format(len(sNext), "b")
#     return [count, zeroCount]


# 풀이 2
# 객체형으로 바꿔본 답변
class Solution:            
    def __init__(self, s):
        self.s = s
        self.count = self.zeroCount = 0
        self.sNext = ""
        
    def solution(self):   
        while self.isOneLength(self.s):
            self.calculate()
        answer = [self.count, self.zeroCount]
        return answer
    
    def isOneLength(self, s):
        return len(s) != 1

    def calculate(self):
        self.removeZero()
        self.countAdd()
        self.changeLenghtToBinary()  

    def removeZero(self):
        self.sNext = self.s.replace("0","") #아하

    def countAdd(self):
        self.count += 1
        self.zeroCount += len(self.s) - len(self.sNext)
    
    def changeLenghtToBinary(self):
        self.s = format(len(self.sNext), "b")

def solution(s):
    return Solution(s).solution()


print(solution("110010101001"))
