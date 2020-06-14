"""回文词判断"""

from Queue.deque import Deque

def palchecker(aString):
    # 初始化双端队列
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    # 是否相等标志
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker('radar'))