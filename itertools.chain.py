'''
# 1. itertools 에서 Chain 내장함수 사용하기

from itertools import chain    

A = [1,2,3,4,5]
B = ['A',"B","c","D","E"]

"""
def chain(*iterables):         # 첫 번째 iterable에서 소진될 때까지 요소를 반환한 다음 iterable로 넘어감. 모든 이터러블이 소진될 때까지 반복
    for i in iterables:        # For문 내에서 For문을 써서 구현
        for j in i:
            yield(j)
"""

print(list(chain(A, B)))
# >>>  [1, 2, 3, 4, 5, 'A', 'B', 'C', 'D', 'E']


# 함수 선언하지 않고 For문으로 작성한 것
"""
iterables = [A,B]

for i in iterables:
    for j in i:
        print(j, end = ' ')
"""

# 넘파이 Concatenate 함수와 비슷하다. 인수로 iterable한 객체를 받아서 객체 내부의 모든 요소들을 이어 붙이는 개념.
'''








