"""实现一个双端队列"""

class Deque:
    def __init__(self):
        """初始化一个双端队列"""
        self.items = []

    def isEmpty(self):
        """判断是否为空"""
        return self.items == []

    def addFront(self, item):
        """队头，入队"""
        self.items.append(item)

    def addRear(self, item):
        """队尾，入队"""
        self.items.insert(0, item)

    def removeFront(self):
        """队头，出队"""
        return self.items.pop()

    def removeRear(self):
        """队尾，出队"""
        return self.items.pop(0)

    def size(self):
        """队列大小"""
        return len(self.items)