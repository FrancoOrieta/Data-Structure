from heap_queue import HeapQueue

heap = HeapQueue()

heap.enqueue(1)
heap.enqueue(2)
heap.enqueue(3)
heap.enqueue(4)
heap.enqueue(5)

print("HeapQueue".center(26, "*"))
print(heap._data,"\n")

print("Longitud".center(26, "*"))
print(len(heap),"\n")

print("Primero".center(26, "*"))
print(heap.first(),"\n")

print("Sacando primero".center(26, "*"))
print(heap.dequeue(),"\n")

print("Nuevo Primero".center(26, "*"))
print(heap.first())
