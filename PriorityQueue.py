class PriorityQueue:

    # Функция сортирует дерево
    def SortTree(array, n, i):
        # Находим самое большое значение среди 
        # корневого, правого и левого дочернего элемента
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[i] < array[left]:
            largest = left

        if right < n and array[largest] < array[right]:
            largest = right

        # Меняем местами и продолжаем сортировку, 
        # если значение корневого элемента не самое большое
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            PriorityQueue.SortTree(array, n, largest)

    # Функция вставляет элемент
    def AddElement(array, newNum):
        size = len(array)
        if size == 0:
            array.append(newNum)
        else:
            array.append(newNum)
            i = size 
            while i >= 0:
                PriorityQueue.SortTree(array, size, i)
                i -= 1

    # Функция удаляет элемент
    def DeleteElement(array, num):
        size = len(array)
        if size > 0:
            tmp = -1
            for i in range(size):
                if array[i] == num:
                    tmp = i
                    break
            if tmp >= 0:
                array.pop(tmp)
                size -= 1
                i = size 
                while i >= 0:
                    PriorityQueue.SortTree(array, size, i)
                    i -= 1
            else:
                print("Такого элемента нет в очереди")
        else:
            print("Очередь пуста!")

    # Функция показывает колчество элементов
    def GetLenQueue(array):
        print("Всего элементов в очереди: " + str(len(array)))

    # Функция показывает максимальный элемент из кучи
    def GetMaxElementQueue(array):
        print("Максимальный элемент кучи равен: " + str(array[0]))

    # Функция проверяет кучу на пустоту 
    def EmptyQueue(array):
        size = len(array)
        if size > 0:
            print("Очередь не пуста, в ней " + str(size)+ " элемент/элементов")
        else:
            print("Очередь пуста!")