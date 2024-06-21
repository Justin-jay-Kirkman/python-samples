from heapq import heapify, heappush, heappop

def inv(val):
    return val * -1

# Creating empty heap
heap = []
heap_max = []
heapify(heap)

# Adding items to the heap using heappush function
heappush(heap, -10)
heappush(heap, -30)
heappush(heap, -20)
heappush(heap, -25)
heappush(heap, -400)

# printing the value of minimum element
print("Head value of heap : " + str(inv(heap[0])))

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(inv(i), end=' ')
print("\n")

element = heappop(heap)

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(inv(i), end=' ')