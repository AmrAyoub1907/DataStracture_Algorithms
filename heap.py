class Minheap:
    size = 0
    items = []
    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1) / 2

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.items[self.getParentIndex(index)]

    def peek(self):
        return self.items[0]

    def poll(self):
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return item

    def add(self, val):
        self.items.append(val)
        self.size += 1
        self.heapifyUp()

    def swap(self, ind1, ind2):
        self.items[ind1], self.items[ind2] = self.items[ind2], self.items[ind1]

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) > self.items[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)

            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            if self.items[index] < self.items[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)

            index = smallerChildIndex


x = Minheap()
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
for i in arr:
    x.add(i)
for i in range(0,len(x.items)):
    print x.poll()