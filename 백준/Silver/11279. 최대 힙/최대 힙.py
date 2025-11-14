#일단은 직접 구현을 해보겠습니다
import sys
input = sys.stdin.readline
# output = sys.stdout.write

def insert_heap(x):
    heap.append(x)
    child = len(heap) - 1
    while child > 0 :
        parent = (child-1) // 2
        if heap[child] > heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent
        else: break
        
def remove_heap():
    heap_size = len(heap)
    if heap_size == 0:
        return 0
    if heap_size == 1:
        return heap.pop()
    max_value = heap[0]
    heap[0] = heap.pop()
    i = 0
    heap_size -= 1
    
    while i < heap_size:
        leftchild = 2*i + 1
        rightchild = 2*i + 2
        largest_idx = i
        
        if leftchild < heap_size and heap[leftchild] > heap[largest_idx]:
            largest_idx = leftchild
        if rightchild < heap_size and heap[rightchild] > heap[largest_idx]:
            largest_idx = rightchild
            
        if largest_idx != i:
            heap[i], heap[largest_idx] = heap[largest_idx], heap[i]
            i = largest_idx
        else:
            break 
    return max_value

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x == 0:
        print(remove_heap())
        # result = remove_heap()
        # output(str(result) + '\n')
    else:
        insert_heap(x)