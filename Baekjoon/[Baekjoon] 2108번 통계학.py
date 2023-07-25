# 통계학

# 조건) 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 
# 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

## 산술평균 : N개의 수들의 합을 N으로 나눈 값
## 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
## 최빈값 : N개의 수들 중 가장 많이 나타나는 값
##          -> @@ 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
## 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
"""
[input과 sys.stdin.readline의 차이점]

- input()이 호출되면 인자로 주어진 문자를 화면에 출력하고 사용자의 입력을 기다린다.
사용자가 키를 누르면 그에 대응하는 데이터가 하나씩 버퍼에 들어간다.
개행 문자는 입력의 종료로 간주한다.
무엇을 입력하든 문자열로 변환하고 줄 바꿈을 제거한 뒤 값을 반환한다.
 
- sys.stdin.readline()
input()과 달리 문자를 화면에 출력하는 기능이 없다.
한 번에 읽을 수 있는 글자 수 크기에 대한 매개변수를 제공한다.
한 번에 읽어와 버퍼에 저장한다. 따라서 하나 씩 누를 때마다 데이터를 버퍼에 저장하는 input() 보다 빠르며 
입력이 많아질수록 차이가 더욱 커진다.
 
- 결론
input()은 문자열 변환, 줄 바꿈 제거 등 추가적인 과정이 있고, 데이터가 하나 씩 버퍼에 들어가는 반면 
sys.stdin.readline()은 문자열로 변환, 줄 바꿈 과정이 없으며 데이터가 한 번에 버퍼에 들어가므로 
sys.stdin.readline()이 input() 보다 빠르다.
"""

# Setting
N = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
num_list = sorted(num_list)

# A1. 직접 구현 방식 -> runtime error
print(round(sum(num_list)/N)) # 산술평균
print(num_list[N//2]) # 중앙값 -> N은 홀수이기 때문에 단순히 몫으로만 고려

# 최빈값 -> 등장 횟수를 딕셔너리에 담기 위해 defaultdict 활용, 기본 value 0으로 시작
from collections import defaultdict
count = defaultdict(int)

for i in num_list:
    count[i] += 1
mode_count = max(count.values()) # 값, 등장빈도를 key, value로 세팅 및 최대 value 추출

mode_list = [] # 최대 반복 해당하는 key 추출 위해 반복문, 미리 sort 해뒀기 때문에 1번째 값 추출(조건에 맞춰서)
for k, v in count.items():
    if v == mode_count:
        mode_list.append(k)
    else:
        pass
mode_list.sort()

print(mode_list[1] if len(mode_list) > 1 else mode_list[0])

# 범위
print(max(num_list) - min(num_list)) 



# A2. statistics 통해 구현 -> 아주 간단
import statistics
print(round(statistics.mean(num_list)))
print(statistics.median(num_list))
mode = statistics.multimode(num_list)
mode.sort()
print(mode[1] if len(mode) > 1 else print(mode[0]))
print(max(num_list) - min(num_list))


# A3. Counter 통해 구현 -> 가장 많은 풀이 방식
from collections import Counter

mode = Counter(num_list).most_common()
print(mode[1] if len(mode) > 1 else print(mode[0]))
