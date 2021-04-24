class linkedList:
    class node:
        def __init__(self, obj):
            self.obj = obj
            self.next = None

        def __repr__(self):
            return 'Object: {}'.format(self.obj)
        
    def __init__(self):
        self.head = None

    def printL(self):
        temp = self.head
        while temp:
            print(temp.obj)
            temp = temp.next

    def insert(self, i, obj):
        temp = self.head
        
        if i == 0:
            self.head = obj
            self.head.next = temp
        else:
            for x in range(i-1):
                temp = temp.next
                
            obj.next = temp.next
            temp.next = obj



    def delete(self, i):
        temp = self.head

        for x in range(i):
            if x + 1 == i:
                deletingNode = temp.next
                temp.next = temp.next.next
                deletingNode = None
                break
            temp = temp.next
            


L = linkedList()
L.head = L.node(5)
L.insert(1, L.node(23))
L.insert(1, L.node(20))
L.insert(0, L.node(1))
