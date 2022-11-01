

# itertools 에서 accumulate 내장함수 사용하기

from itertools import accumulate
import operator

'''
# accumulate 호출하면 있는 기본적인 
def accumulate(iterable, func=operator.add, *, initial = None):      # func = operator.add, initial = None이 디폴트 값
    it = iter(iterable)                                              # iterable을 iterator로 만듬
    total = initial

    if initial is None:
        try:
            total = next(it)                      # iterator를 next를 이용해 total값을 it의 첫 번째 요소가 들어가도록 함
        except StopIteration:
            return
    yield total                                   # total값으로 it의 첫 번째 요소가 yield  // initial이 None이 아니라면 지정된 initial값이 출력됨
    for element in it:                            # for문으로 it의 2번째 요소부터 내부를 돌면서 total + element를 수행   
        total = func(total, element)
        yield total                               # 최종적인 total 값 yield

'''

'''
def accumulate(iterable, func = operator.truediv, initial = None):            # truediv = 나눗셈의 결과를 반환
    it = iter(iterable)                                              # iterable을 iterator로 만듬
    total = initial

    if initial is None:
        try:
            total = next(it)                      # iterator를 next를 이용해 total값을 it의 첫 번째 요소가 들어가도록 함
        except StopIteration:
            return
    yield total                                   # total값으로 it의 첫 번째 요소가 yield
    for element in it:                            # for문으로 it의 2번째 요소부터 내부를 돌면서 total + element를 수행
        total = func(total, element)
        yield total               

'''



A = [1,-2,-3,4,5]

print(list(accumulate(A, initial = 100)))                     # initial 값으로 100을 줌

print(list(accumulate(A, func= max)))                         # func을 max로 선언 --> iterable을 돌면서 max값이 출력