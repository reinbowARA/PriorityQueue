from PriorityQueue import PriorityQueue


if __name__ == "__main__":
    test = PriorityQueue()
    test.AddElement(1)
    test.AddElement(1)
    test.AddElement(2)
    test.AddElement(1)
    test.AddElement(3)
    test.AddElement(-4)

    print ("Массив max-кучи: " + str(test.GetQueue()))

    test.DeleteElement(1)
    print("После удаления элемента: " + str(test.GetQueue()))

    test.GetLenQueue()

    test.GetMaxElementQueue()

    test.EmptyQueue()