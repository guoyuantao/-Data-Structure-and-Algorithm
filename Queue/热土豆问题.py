"""击鼓传花或者约瑟夫问题"""
from Queue.queue import Queue

def hotPotato(namelist, num):
    # 初始化一个队列
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):  # 传递次数
            # 一次传递
            simqueue.enqueue(simqueue.dequeue())
        # 传递完num次之后，删除花所在位置
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))