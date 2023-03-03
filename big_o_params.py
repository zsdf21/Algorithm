# big_O는 실행 시간에서 Python 코드의 시간 복잡도를 추정하는 Python 모듈
# big_O는 증가하는 크기 N 의 입력에 대해 Python 함수를 실행 하고 실행 시간을 측정
from big_o_params import positive_int_generator
import big_o

import big_o

# def find_max(x):
#      """Find the maximum element in a list of positive integers."""
#      max_ = 0
#      for el in x:
#          if el > max_:
#              max_ = el
#      return max_

best, others = big_o.big_o(reverse_str, positive_int_generator, n_repeats=100)

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)