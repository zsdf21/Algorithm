# Q14. 정렬되어 있는 두 연결 리스트를 합쳐라
import typing
import collections
from collections import deque
import time

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 연결 리스트 생성
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(3)
node6 = ListNode(5)
node4.next = node5
node5.next = node6

start_time = time.time()
time.sleep(1)

def mergelist(l1, l2):
    if not l1 or (l2 and (l1.val > l2.val)):
        l1, l2 = l2, l1
    
    if l1:
        l1.next = mergelist(l1.next, l2)
    return l1

result = mergelist(node1, node4)

# palin(input_str)
end_time = time.time()
time_ = end_time - start_time

# print("result:", result)
while result:
    print(result.val)
    # 출력 후 다음으로 넘어가기
    result = result.next

print(f'time: {time_:.3f}')