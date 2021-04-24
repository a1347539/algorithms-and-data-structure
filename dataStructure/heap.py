class maxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        i+=1
        if i == 1:
            return None
        return (i-1) // 2

    def leftChild(self, i):
        if i * 2 > self.size:
            return None
        return i * 2

    def rightChild(self, i):
        if i * 2 + 1 > self.size:
            return None
        return i* 2 + 1

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, i, up):
        if up:
            while self.parent(i) != None and self.heap[i] > self.heap[self.parent(i)]:
                self.swap(i, self.parent(i))
                i = self.parent(i)
        if not up:
            while True:
                if (self.leftChild(i) != None or self.rightChild(i) != None):
                    if (self.heap[i] < self.heap[self.leftChild(i)]
                    or self.heap[i] < self.heap[self.rightChild(i)]):
                        if (self.heap[self.leftChild(i)] < self.heap[self.rightChild(i)]):
                            self.swap(i, self.rightChild(i))
                            i = self.rightChild(i)
                        else:
                            self.swap(i, selfleftChild(i))
                            i = self.leftChild(i)
                else:
                    break

    def insert(self, i, obj):
        self.size += 1;
        self.heap.insert(i, obj)
        self.heapify(i, True)

    def append(self, obj):
        self.size += 1;
        self.heap.append(obj)
        self.heapify(len(self.heap)-1, True)    

    def delete(self, i):
        self.size -= 1;
        self.swap(i, -1)
        self.heap.pop()
        self.heapify(i, False)


h = maxHeap()
h.append(5)
h.append(21)
h.append(43)
h.append(534)
h.append(2)
