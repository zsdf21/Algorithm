# Q13. 연결 리스트가 팰린드롬 구조인지 판별하라.
import typing
import collections
from collections import deque
import time

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
# def add(data):
#     node = head
#     # next가 존재하지 않을 때 까지
#     while head.next:
#         node = head.next
#     node.next = Node(data)


start_time = time.time()
time.sleep(1)

## 연결 리스트 생성
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node5 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

input_str = [1, 2, 2, 2, 1]

# ###### ver1 #######
# def palin(s):

#     for i in range(len(s)):
#         if s[i] == s[len(s)-i-1]:
#             return True
#         else: 
#             return False

####### ver2 ####### 기본, list 이용

# def palin(s: ListNode):
#     q: List = []

#     if not s:
#         return True
    
#     node = s
#     # 리스트 변환
#     while node is not None:
#         q.append(node.val)
#         node = node.next

#     # 팰린드롬 판별
#     while len(q) > 1:
#         if q.pop(0) != q.pop(): # list의 .pop(0)은 O(n)임, O(1)로 개선 가능해보임.
#             return False
        
#     return True

####### ver3 ####### deque 이용

def palin(s):

    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not s:
        return True
    
    node = s
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) >1 :
        if q.popleft() != q.pop():
            return False
    
    return True

####### ver4 ####### 런너 이용
def palin(s):

    rev = None
    slow = fast = s

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast: # 홀수인 경우 중앙 1개
        slow = slow.next

    # 팰린드롬 확인 파트
    while slow and slow.val == rev.val:
        slow, rev = slow.next, rev.next

    return not slow

result = palin(node1)

# palin(input_str)
end_time = time.time()
time_ = end_time - start_time

print("result:", result)
print(f'time: {time_:.3f}')