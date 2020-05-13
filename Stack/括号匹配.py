"""
在数学运算中，括号需要是匹配的。编写程序判断括号是否匹配。
思路：
1. 初始化一个空栈
2. 遍历括号，如果是左括号，入栈
3. 如果是右括号，如果栈顶元素是左括号，则出栈，消去。
4. 当右括号仍存在，栈以空。或者栈不空，右括号扔存在。则不匹配。
"""

from Stack.stack import Stack

def parChecker(symbolString):
    """
    简单括号是否匹配
    :param symbolString: 括号字符串
    :return: bool型，匹配：True，不匹配：False
    """
    # 初始化一个栈
    s = Stack()
    # 是否匹配标志
    balanced = True
    # 下标
    index = 0
    # 遍历
    while index < len(symbolString) and balanced:
        # 取出字符
        symbol = symbolString[index]
        # 如果为左括号，则入栈
        if symbol == '(':
            s.push(symbol)
        else:
            # 当字符不为左括号，如果栈为空，则不匹配
            if s.isEmpty():
                balanced = False
            # 如果栈不空，则将左括号出栈
            else:
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

test_str1 = '((()))'
test_str2 = '((())'
print(parChecker(test_str1))
print(parChecker(test_str2))


