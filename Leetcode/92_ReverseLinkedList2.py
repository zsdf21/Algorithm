# Q19. 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스m은 1부터 시작한다. 
import time

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 연결 리스트 생성
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

start_time = time.time()
time.sleep(1)

def reverseBetween(head: ListNode, m, n):
    
    # 예외 처리
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head
    
    # start 및 end 지정
    for _ in range(m-1):
        start = start.next
    end = start.next
    
    # 반복하면서 노드 차례로 뒤집기
    for _ in range(n-m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
        
    return root.next



result = reverseBetween(node1, 2, 4)
end_time = time.time()
print("result:", result)

while result:
    print(result.val)
    # 출력 후 다음으로 넘어가기
    result = result.next

time_ = end_time - start_time
print(f'time: {time_:.3f}')