class PriorityQueue:

    def __init__(self):
        self.array = []
        self.size = 0

    # Функция сортирует дерево
    def SortTree(self, n, i):
        # Находим самое большое значение среди 
        # корневого, правого и левого дочернего элемента
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self[i] < self[left]:
            largest = left

        if right < n and self[largest] < self[right]:
            largest = right

        # Меняем местами и продолжаем сортировку, 
        # если значение корневого элемента не самое большое
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            PriorityQueue.SortTree(self, n, largest)

    # Функция вставляет элемент
    def AddElement(self, newNum):
        self.array.append(newNum)
        self.size += 1
        i = self.size 
        while i >= 0:
            PriorityQueue.SortTree(self.array, self.size, i)
            i -= 1

    # Функция удаляет элемент
    def DeleteElement(self, num):
        size = self.size
        if size > 0:
            tmp = -1
            for i in range(size):
                if self.array[i] == num:
                    tmp = i
                    break
            if tmp >= 0:
                self.array.pop(tmp)
                size -= 1
                i = size 
                while i >= 0:
                    PriorityQueue.SortTree(self.array, size, i)
                    i -= 1
            else:
                print("Такого элемента нет в очереди")
        else:
            print("Очередь пуста!")

    # Функция показывает колчество элементов
    def GetLenQueue(self):
        print("Всего элементов в очереди: " + str(len(self.array)))

    # Функция показывает максимальный элемент из кучи
    def GetMaxElementQueue(self):
        print("Максимальный элемент кучи равен: " + str(self.array[0]))

    # Функция проверяет кучу на пустоту 
    def EmptyQueue(self):
        size = self.size
        if size > 0:
            print("Очередь не пуста, в ней " + str(size)+ " элемент/элементов")
        else:
            print("Очередь пуста!")

    # Функция показывающая очередь
    def GetQueue(self):
        return self.array