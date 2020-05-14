"""实现一个队列"""
class Queue:
    def __init__(self):
        """初始化一个列表空间，作为队列"""
        self.items = []

    def isEmpty(self):
        """判断是否为空"""
        return self.items == []

    def enqueue(self, item):
        """入队"""
        self.items.insert(0, item)

    def dequeue(self):
        """出队"""
        return self.items.pop()

    def size(self):
        """统计队列大小"""
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue('true')
    q.enqueue('5')
    q.enqueue(6)
    print(q.items)
    q.dequeue()
    print(q.items)
    print(q.isEmpty())
    print(q.size())