import time
# 普通递归方法
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins
start = time.time()
ret = recMC([1, 5, 10, 25], 63)
end = time.time()
print(f"运行结果：{ret}, 运行时间：{end - start}")

# 递归解法改进
def recDC(coinValueList, change, knowResults):
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]   # 查表成功，直接用最优解
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knowResults)

            if numCoins < minCoins:
                minCoins = numCoins
                # 找到最优解，记录到表中
                knowResults[change] = minCoins
    return minCoins

start = time.time()
ret = recDC([1, 5, 10, 25], 63, [0] * 64)
end = time.time()
print(f"改进版运行结果：{ret}， 改进版运行时间：{end - start}")