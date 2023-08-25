# 용액
"""
KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 
각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 
산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 
알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 
이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 

예를 들어, 주어진 용액들의 특성값이 [-99, -2, -1, 4, 98]인 경우에는 특성값이 -99인 용액과 
특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 
이 용액의 특성값이 0에 가장 가까운 용액이다. 
참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 
특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때, 
이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 
두 용액을 찾는 프로그램을 작성하시오.

# 입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.


# 출력
첫 번째 줄에는 총 단지수를 출력하시오. 
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split())) # 이미 오름차순으로 투입

# A1) Two Pointer
answer = float("inf")
l, r = 0, N-1
l_value, r_value = 0, 0

while l < r:                    # l, r이 만나기 전까지 진행
    c_value = arr[l] + arr[r]   # c_value(current value)
    
    if abs(c_value) <= answer:  # ans보다 현재 값이 작으면 해당 값을 정답으로 할당
        x = arr[l]
        y = arr[r]
        answer = abs(c_value)
    
    if c_value <= 0:            # c_value <= 0 -> 왼쪽 값을 우측으로 한칸 이동
        l += 1
    else:                       # c_value > 0 -> 오른쪽 값을 좌측으로 한칸 이동
        r -= 1
        
print(x, y)

# A2) Binary Search -> 투 포인터 대비 시간 소요 큼. 
answer = float("inf")
l, r = 0, N-1

for i in range(N-1): # i <-> [low - high]까지의 값의 합을 이진탐색으로 구하여 0에 가까운 쌍을 찾는 방식
    low = i + 1      # i와 합   
    high = N - 1
    
    while low <= high:              # low와 high가 만날때까지 탐색 진행
        mid = (low + high) // 2     # 기준점 역할을 할 중앙값
        c_value = arr[i] + arr[mid] # i번째 값과 중앙값의 합을 기준으로 탐색 진행
        
        if abs(c_value) < answer:
            l = i
            r = mid
            answer = abs(c_value)
            
        if c_value == 0:            
            break
        elif c_value < 0:           # i번째 값과 중앙값이 0보다 작다 -> 값이 커질 필요
            low = mid + 1
        else:
            high = mid - 1          # i번째 값과 중앙값이 0보다 크다 -> 값이 작아질 필요
            
print(arr[l], arr[r])