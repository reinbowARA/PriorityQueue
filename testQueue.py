from PriorityQueue import PriorityQueue

arr = []

PriorityQueue.AddElement(arr, 1)
PriorityQueue.AddElement(arr, 1)
PriorityQueue.AddElement(arr, 2)
PriorityQueue.AddElement(arr, 1)
PriorityQueue.AddElement(arr, 3)
PriorityQueue.AddElement(arr, -4)

print ("Массив max-кучи: " + str(arr))

PriorityQueue.DeleteElement(arr, 1)
print("После удаления элемента: " + str(arr))

PriorityQueue.GetLenQueue(arr)

PriorityQueue.GetMaxElementQueue(arr)

PriorityQueue.EmptyQueue(arr)