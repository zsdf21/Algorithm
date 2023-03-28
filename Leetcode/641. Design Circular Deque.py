# Q26. 다음 연산을 제공하는 원형 데크를 디자인하라
# 1) 데크 사이즈 k로 지정
# 2) 데크 처음 아이템 추가
# 3) 데크 마지막 아이템 추가
# 4) 데크 처음 아이템 삭제
# 5) 데크 마지막 아이템 삭제
# 6) 데크 첫 아이템 호출
# 7) 데크 마지막 아이템 호출
# 8) 데크가 비어있는 지 여부 판별
# 9) 데크가 가득 차 있는 지 여부 판별

# deque를 이중연결로 구현할 때 head와 tail은 실제 값을 가지지 않고 그냥 포인터
# 앞에 넣을때 -1을 해서 공간을 확보

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        self.right = val.next
        # self.left 
        
class DequeCirculater:
    # 1) 데크 사이즈 k로 지정
    # 데크를 이중 연결 리스트로 구현하기 위해 좌와 우 인덱스 역할을 할 head와 tail 정의, 최대 길이 정보를 k로 설정, 현재 길이 정보는 len에 담을 예정
    def __init__(self, k:int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        
    # 내부에서만 사용한다는 의미로 밑줄 하나로 시작하도록 메소드 명 지정
    # n = node -> / node -> new / node <- new / new -> n, 
    # n은 무의미한 숫자?
    def _add(self, node: ListNode, new:ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    
    def _del(self, node:ListNode):
        n = node.right.right
        node.right = n
        n.left = node
        
    # 2) 데크 처음 아이템 추가
    def insertFront(self, value:int) -> bool:
        # 새 노드 삽입 시 최대 길이에 도달했을 때는 False 리턴
        if self.len == self.k:
            return False
        # 최대 길이가 아닐 경우 _add 메서드를 활용하여 head 위치에 노드 삽입
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
    
    
    # 3) 데크 마지막에 아이템 추가
    def insertLast(self, value:int) -> bool:
        # 새 노드 삽입 시 최대 길이에 도달했을 때는 False 리턴
        if self.len == self.k:
            return False
        # 최대 길이가 아닐 경우 _add 메서드를 활용하여 head 위치에 노드 삽입
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
    
    # 4) 데크 처음 아이템 삭제
    def deleteFront(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
    
    # 5) 데크 마지막 아이템 삭제
    def deleteLast(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
    # 6) 데크 첫 아이템 호출
    def getFront(self): 
        return self.head.right.val if self.len else -1
        # or
        # if self.len :
        #     return self.head.right.val
        # else :
        #     return -1
        
    # 7) 데크 마지막 아이템 호출
    def getRear(self):
        return self.tail.left.val if self.len else -1
        # or
        # if self.len :
        #     return self.tail.left.val
        # else :
        #     return -1

    # 8) 데크가 비어있는 지 여부 판별
    def isEmpty(self):
        return self.len == 0
    
    # 9) 데크가 가득 차 있는 지 여부 판별
    def isFull(self):
        return self.len == self.k
    
    
# 연결 리스트 생성
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node_new_1 = ListNode(6)
node_new_2 = ListNode(7)
node_new_3 = ListNode(8)
node_new_1.next = node_new_2
node_new_2.next = node_new_3

for i in range(3):
    print(node1.val)
    node1 = node1.next

inst = DequeCirculater(3)
inst._add(node1, node_new_2)

        
        
        
# # 연결 리스트 생성
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node6 = ListNode(6)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6

# start_time = time.time()
# time.sleep(1)

# def reverseBetween(head: ListNode, m, n):
    
#     # 예외 처리
#     if not head or m == n:
#         return head

#     root = start = ListNode(None)
#     root.next = head
    
#     # start 및 end 지정
#     for _ in range(m-1):
#         start = start.next
#     end = start.next
    
#     # 반복하면서 노드 차례로 뒤집기
#     for _ in range(n-m):
#         tmp, start.next, end.next = start.next, end.next, end.next.next
#         start.next.next = tmp
        
#     return root.next

# result = reverseBetween(node1, 2, 4)
# end_time = time.time()
# print("result:", result)

# while result:
#     print(result.val)
#     # 출력 후 다음으로 넘어가기
#     result = result.next

# time_ = end_time - start_time
# print(f'time: {time_:.3f}')