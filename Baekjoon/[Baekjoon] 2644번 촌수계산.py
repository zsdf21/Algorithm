# 촌수계산
"""
# 문제
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

# 입력
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

# 출력
입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다."""

import sys
from collections import deque

n = int(sys.stdin.readline())
s, e = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)] # index를 부모-자식 숫자와 맞추기 위해 n+1
visit = [0 for _ in range(n+1)]
# visit

for i in range(m):              # 부모-자식 간 연결 graph에 입력, 양방향 주의
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)          # 인덱스 별 부모-자식 연결
# graph 

############ A1. BFS
def BFS(x, y):
    queue = deque([x])                  # x를 담고
    # print('que:', queue)
    visit[x] = 0
    # print(visit)
    
    while queue:                        # x에서 시작, x와 1촌인 관계부터 탐색
        people = queue.popleft()        # x와 1촌인 사람 탐색 
        
        if people == y:                 # 자기 자신일 경우 0촌
            return visit[y]
        
        for f in graph[people]:         # 1촌의 모든 친척 고려
            if visit[f] == 0:           # x와 f간 관계가 고려되지 않았던 경우
                queue.append(f)         # f를 큐에 입력, 재탐색위해
                visit[f] = visit[people] + 1 # 해당 x와 f간 visit(촌수) +1 
                # print(visit)
                
    return -1

print(BFS(s, e))


############ A2. DFS
def DFS(x):
    for n in graph[x]:
        if check[n] == 0:
            check[n] = check[x]+1
            DFS(n)
            
check = [0]*(n+1)

DFS(s)

print(check[e] if check[e] > 0 else -1)
