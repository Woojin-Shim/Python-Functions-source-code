'''
Brute Force : '가능한 모든 경우를 시도해 보는 것' , 영어 직역하면 난폭한 힘
시간도 오래 걸리고 자원 문제도 있지만 가능한 모든 경우를 계산하여 정확도 100%라는 장점이 있다.
암호학에서 흔히 사용되고 수학계에서도 간혹 사용된다고 함.
파이썬 알고리즘 문제에도 간혹 나오며 보통 1. For,while문  2. 재귀함수 로 구현
'''

# 연속 부분 최대합 구하기(Brute Force 함수 만들어서 풀이)

'''
import sys
import math

def getSubsum(data) :
    result = -math.inf                                                 # inf는 무한대
    temp = 0
    for start in range(len(data)):                                       # start = 0
        for end in range(start, len(data)):                              # end = 0         end = 1
            temp = 0                                                     # temp = 0        temp = 0
            for i in range(start, end+1):                                # i = 0           i = 0            i = 1
                temp += data[i]                                          # temp = data[0]  temp = data[0]   temp = data[0] + data[1]
            result = max(result, temp)                                   # result = temp   result = max(result, temp)
    return result                                                        # 각 for 문을 돌면 모든 경우의 수를 비교하고 그중 가장 큰 값을 도출

def main():
    data = [int(x) for x in input().split()]
    print(getSubsum(data))

if __name__ == "__main__":
    main()
'''

