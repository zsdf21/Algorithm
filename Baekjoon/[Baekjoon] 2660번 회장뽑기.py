# 회장뽑기
"""
# 문제
월드컵 축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 이 모임은 만들어진지 얼마 되지 않았기 때문에 회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다. 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.

예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.

4점, 5점 등은 같은 방법으로 정해진다. 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이라고 본다.

회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.

# 입력
입력의 첫째 줄에는 회원의 수가 있다. 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다. 
회원번호는 1부터 회원의 수만큼 붙어 있다. 마지막 줄에는 -1이 두 개 들어있다.

# 출력
첫째 줄에는 회장 후보의 점수와 후보의 수를 출력하고, 두 번째 줄에는 회장 후보를 오름차순으로 모두 출력한다.
"""

import sys
n = int(sys.stdin.readline())
INF = float('inf')

arr = [[INF] * n for _ in range(n) ] # 관계 여부를 표시할 arr

for i in range(n):  # 예외처리, 자신과의 관계는 0
    arr[i][i] = 0

# 직접 연결된 관계들(1-hop) arr 1 수정
while True:         # -1이 나올 때까지 a, b 할당
    a, b = map(int, sys.stdin.readline().split())
    if a == -1:
        break
    
    arr[a-1][b-1], arr[b-1][a-1] = 1, 1 # 관계가 있을 경우 양방향 수정(inf -> 1)

# 2-hop, 3-hop 등 고려
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][k] + arr[k][j]: # i, j 간 관계가 무한대 -> k를 거친(hop을 고려한) i-k-j 관계로 해당 arr 수정 
                arr[i][j] = arr[i][k] + arr[k][j]

ans = []
for i in range(n):
   ans.append(max(arr[i][:])) # max를 통해 각 사람들의 최대 hop을 구함, 최종적으로 최소 hop을 가진 사람이 회장 후보

min_hop = min(ans)    

res = []

for i in range(n):
   if ans[i]==min_hop:
       res.append(i+1)
       
print(min_hop, ans.count(min_hop))
print(*res)