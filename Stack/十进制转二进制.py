"""
问题:将十进制转换为二进制
思路：除2取余，将结果存入栈，然后按顺序出栈。
"""
from Stack.stack import Stack

def divideBy2(decNumber):
    # 初始化栈
    remstack = Stack()
    # 截止条件为被除数大于0
    while decNumber > 0:
        # 取余数
        rem = decNumber % 2
        # 余数入栈
        remstack.push(rem)
        # 更新被除数
        decNumber = decNumber // 2

    # 当栈不空的时候，出栈
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))