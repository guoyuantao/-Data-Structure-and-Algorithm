

def moveTower(height, fromPole, withPole,  toPole):
    """
    汉诺塔问题
    :param height: 汉诺达的高度
    :param fromPole: 初始桩
    :param withPole: 中间桩
    :param toPole: 目标桩
    :return:
    """
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)  # 将height-1个盘移动到中间桩
        moveDisk(height, fromPole, toPole)  # 最大盘移动到目标桩
        moveTower(height - 1, withPole, fromPole, toPole)  # 将height-1个盘从中间桩经由初始桩移动到目标桩

def moveDisk(disk, fromPole, toPole):
    print(f"Moving disk[{disk}] form {fromPole} to {toPole}")

moveTower(3, "#1", "#2", "#3")