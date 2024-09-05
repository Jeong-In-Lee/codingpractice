
#시간 초과 (아무래도 O(n^2) 이라 그런 듯)
import heapq
import copy

def firstTry():
    N = int(input())
    heap = []
    for i in range(N):
        heapq.heappush(heap, int(input()))
        temp = copy.copy(heap)
        if i==0:
            print(heap[0])
        elif i%2==0:
            n=i//2-1
            while n>0:
                n-=1
                heapq.heappop(temp)
            print(temp[0])
        else:
            n=i//2
            while n>0:
                n-=1
                heapq.heappop(temp)
            print(temp[0])


# sys로 input 바꾸고 통과
def answer():
    N = int(input())
    leftHeap = [] #최대힙
    rightHeap = [] #최소힙
    mid = 0
    for i in range(N):
        num = int(input())
        if i==0:
            mid = num
            print(mid)
        elif num>=mid:
            heapq.heappush(rightHeap, num)
            if len(rightHeap)-len(leftHeap)>=2:
                heapq.heappush(leftHeap, -1*mid)
                mid = heapq.heappop(rightHeap)
            print(mid)
        else:
            heapq.heappush(leftHeap, -1*num)
            if len(leftHeap)-len(rightHeap)>=2:
                heapq.heappush(rightHeap, mid)
                mid = -1*heapq.heappop(leftHeap)
            print(mid)