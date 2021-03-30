import sys
class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize+1)
        self.Heap[0] = sys.maxsize
        self.Front = 1

    def parent(self, pos):
        return pos//2

    def leftChild(self, pos):
        return pos*2

    def rightChild(self, pos):
        return pos*2+1

    def isLeaf(self, pos):
        if pos * 2 > self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def maxheapify(self, pos):
        if not self.isLeaf(pos):
            if self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[self.rightChild(pos)]:
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.rightChild(pos))
                    self.maxheapify(self.rightChild(pos))
                else:
                    self.swap(pos, self.leftChild(pos))
                    self.maxheapify(self.leftChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size+=1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print(self):
        for n in range(1, self.size//2+1):
            print("parent:", self.Heap[n], "Left:", self.Heap[n*2], "right:", self.Heap[n*2+1], "\n")

    def extractmax(self):
        popped = self.Heap[self.Front]
        self.swap(self.Front, self.size)
        self.size-=1
        self.maxheapify(self.Front)
        return popped

maxHeap = MaxHeap(15)
maxHeap.insert(4)
maxHeap.insert(3)
maxHeap.insert(6)
maxHeap.insert(3)
maxHeap.insert(6)
maxHeap.insert(2)
maxHeap.print()










        
