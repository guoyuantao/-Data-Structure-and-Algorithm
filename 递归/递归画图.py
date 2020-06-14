import turtle

t = turtle.Turtle()

def drawSpiral(t, lineLen):
    if lineLen > 0:   # 递归结束条件。最小规模，0直接退出
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t, lineLen - 5)

drawSpiral(t, 100)
turtle.done()