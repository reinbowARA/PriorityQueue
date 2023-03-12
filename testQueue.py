from PriorityQueue import PriorityQueue


if __name__ == "__main__":
    test = PriorityQueue()
    test.AddElement(9)
    test.AddElement(7)
    test.AddElement(3)
    test.AddElement(5)
    test.AddElement(6)

    print ("Массив max-кучи: " + str(test.GetQueue()))

    test.DeleteElement(5)
    print("После удаления элемента: " + str(test.GetQueue()))

    test.GetLenQueue()

    test.GetMaxElementQueue()

    test.EmptyQueue()