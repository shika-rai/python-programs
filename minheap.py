import heapq
elements=[20,40,30,1,3,6,2,5,36]
min_heap=[]
for i in elements:
    heapq.heappush(min_heap,i)
print(min_heap)
a=heapq.heappop(min_heap)
print(a)    