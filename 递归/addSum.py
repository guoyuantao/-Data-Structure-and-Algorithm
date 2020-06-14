# 用递归的方式求和

def Sum(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + Sum(alist[1:])

print(Sum(alist=[1, 2, 3, 4]))