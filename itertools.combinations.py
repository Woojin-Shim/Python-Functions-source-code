
# itertools에서 combinations 내장함수 사용하기   (Combinations 조합 : n개 중 순서 상관없이 r개를 고르는 것)   nCr

# from itertools import combinations

def combinations(iterable, r):
    pool = tuple(iterable)                        # iterable 객체 tuple형식 저장
    n = len(pool)                                 # n = 객체 원소 개수
    if r > n:                                     
        return
    indices = list(range(r))                      # indices = [0,1,x,x,,,,r-1]
    yield tuple(pool[i] for i in indices)         # (pool[0], pool[1], pool[2],,,pool[r-1])
    while True:
        for i in reversed(range(r)):              #      reversed 객체  [r-1,,,,x,x,1,0]
            if indices[i] != i + n - r:           #    indices[r-1] != r-1 + n - r  >>>> break 
                break
        else:
            return
        indices[i] += 1                            # indices[r-1] += 1
        for j in range(i+1, r):                    #  
            indices[j] = indices[j-1] + 1          # indices[i+1] = indices[i] + 1
        yield tuple(pool[i] for i in indices)

a = list(combinations([1,2,3], 2))

print(a)

'''
iterable = [1,2,3]  , r = 2  로 설정
pool = (1,2,3)
n = 3
indices = [0,1]
yield tuple(pool[0], pool[1])                                     >> (1, 2)를 yield함

for i in reversed(range(2)):   >>  for i in [1,0]
    if indices[1] != 1 + n - r:      >> 1  !=  1 + 3 - 2
        다르므로 break 후 넘어감

indices[1] = indices[1] + 1    >> indices = [0,2]

for j in range(2,2):           >> None

yield tuple(pool[i] for i in indices)
(pool[0], pool[2])                                                >> (1, 3)을 yield함

다시 while문 밑의 for문으로 돌아간다.
    if indices[i] != i + 3 - 2:      i = 1 일 때   2 != 1+3-2 로 다르지 않으므로 i = 0 대입  indices[0] != 1은 성립하므로 i = 0으로 넘어감   
        break

    indices[0] = indices[0] + 1   >> indices = [1,2]

for j in range(1,2):
    indices[1] = indices[0] + 1    >> indices = [1,2]

    (pool[1], pool[2]) 를 yield함                                 >> (2,3)을 yield함


다시 while문 밑의 for문으로 돌아간다.
 i = 1 , i = 0 모두 같은 값이 나와서 else:문 return을 통해 식을 빠져나옴


'''