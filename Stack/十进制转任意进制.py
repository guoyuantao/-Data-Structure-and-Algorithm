"""
将十进制的数转换为任意进制的数
"""
from Stack.stack import Stack

def baseConberter(decNumber, base):
    # 定义字符
    digits = '0123456789ABCDEF'
    # 初始化栈
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConberter(25, 2))
print(baseConberter(25, 16))