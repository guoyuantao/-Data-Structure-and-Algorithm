""" 定义一个栈 """
class Stack:
    def __init__(self):
        """初始化一个栈"""
        self.items = []

    def isEmpty(self):
        """判断栈是否为空"""
        return self.items == []

    def push(self, item):
        """入栈"""
        return self.items.append(item)

    def pop(self):
        """出栈"""
        self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items) - 1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)

if __name__ == '__main__':
    stack = Stack()
    stack.push(4)
    stack.push('true')
    stack.push(True)
    print(stack.items)
    print(stack.isEmpty())
    stack.pop()
    print(stack.items)
    print(stack.peek())
    print(stack.size())