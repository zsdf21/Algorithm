# 컨베이어 벨트 위의 로봇
'''
컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 한다. 로봇을 옮기는 과정에서는 아래와 같은 일이 순서대로 일어난다.

벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번째 단계이다.
'''

'''
입력
첫째 줄에 N, K가 주어진다. 둘째 줄에는 A1, A2, ..., A2N이 주어진다.
2 ≤ N ≤ 100
1 ≤ K ≤ 2N
1 ≤ Ai ≤ 1,000

출력
몇 번째 단계가 진행 중일때 종료되었는지 출력한다.
'''

# A1. List로 접근(직관적이나 느림)
import sys

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0]*N

ans = 0

while True:
    ans += 1
    
    # phase 1. 벨트 및 로봇 회전, N-1에 위치한 로봇 내림
    belt = [belt[-1]] + belt[:-1]   # 제일 뒤에 위치한 belt 가장 앞으로 밀어넣기
    robot = [0] + robot[:-1]        # 제일 앞 0 밀어넣고 나머지 로봇 한칸씩 뒤로 위치시키기
    robot[N-1] = 0                  # N-1에 위치한 로봇 내리기

    # phase 2. 로봇 한칸씩 이동(먼저 올라간 것부터)
    for i in range(N-2, 0, -1): # N-1 로봇은 이미 내려감, 먼저 올라간 것부터 처리하기 위해 역순으로 진행
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i], robot[i+1] = 0, 1 # 로봇 한칸 이동
            belt[i+1] -= 1              # 옮긴 벨트 내구도 감소

    # phase 3. belt[0]에 새로운 로봇 올리기(내구도 > 0 일때)
    if belt[0] > 0:
        robot[0] = 1    # 시작지점 로봇 올리기
        belt[0] -= 1    # 시작지점 내구도 감소
    
    # phase 4. 내구도 0 개수 K 이상 시 break
    if belt.count(0) >= K:
        break
    
print(ans)



########################################################
# Ans2) List 개선(시간 감소 5배 이상, count가 핵심적)
## (1. 매번 count 비효율적 -> 내구도 0 발생 시 cnt+1 / 2. 리스트 연산 효율성 위해 insert, pop 사용)
ans = 0
cnt = 0
while True:
    ans+=1
    
    # phase 1. 벨트 및 로봇 회전, N-1에 위치한 로봇 내림
    belt.insert(0, belt.pop()) # pop -> 제일 끝에 걸 꺼내서 0자리에 투입
    robot.pop()                # 로봇은 내려가기만 하기에 pop만 수행 
    robot.insert(0, 0)         # 이후 로봇 제일 앞 0 투입
    robot[N-1]=0

    # phase 2. 로봇 한칸씩 이동(먼저 올라간 것부터)           
    for i in range(N-2, 0, -1): 
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i], robot[i+1] = 0, 1 
            belt[i+1] -= 1              
            if belt[i+1]==0:    # 내구도가 감소해서 0이되면 cnt 1증가
                cnt+=1

    # phase 3. belt[0]에 새로운 로봇 올리기(내구도 > 0 일때)     
    if belt[0] > 0:
        robot[0] = 1    
        belt[0] -= 1    
        if belt[0] == 0:        # 내구도가 감소해서 0이되면 cnt 1증가
            cnt += 1

    # phase 4. 내구도 0 개수 K 이상 시 break
    # if belt.count(0) >= K:
    #     break
    if cnt>=K:                  # 매번 카운트 -> 비효율적, 단일 비교 수행
        break

print(ans)



##############################################################
# Ans3) 가장 많이 활용된 deque 구조 활용 -> list 대비 40%가량 시간단축
## deque: deque는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형으로, 스택(stack)처럼 써도 되고 큐(queue)처럼 써도 됨.

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
belt = deque(list(map(int, sys.stdin.readline().split())))

def solution(N, K, belt):
    ans = 0
    robot = deque([0] * N)

    while True:
        ans += 1

        # phase 1. 벨트 및 로봇 회전, N-1에 위치한 로봇 내림
        belt.rotate(1)
        robot.rotate(1)
        robot[N-1] = 0

        # phase 2. 로봇 한칸씩 이동(먼저 올라간 것부터)
        for i in range(N-2, 0, -1):
            if robot[i] and not robot[i+1] and belt[i+1] > 0: # == 0 or not 선택
                robot[i], robot[i+1] = 0, 1
                belt[i+1] -= 1
        
        
        # phase 3. belt[0]에 새로운 로봇 올리기(내구도 > 0 일때)     
        if belt[0] > 0:
            robot[0] = 1
            belt[0] -= 1
        
        # phase 4. 내구도 0 개수 K 이상 시 break
        if belt.count(0) >= K:
            break

    return ans

print(solution(N, K, belt))