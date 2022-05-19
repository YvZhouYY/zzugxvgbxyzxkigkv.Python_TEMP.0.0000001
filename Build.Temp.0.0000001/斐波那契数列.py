# -*- coding: UTF-8 -*-
from sympy import sqrt,expand
from os import _exit

reply = str('Y')
while reply in "Yy":

    #计算数值
    n = int(input("The Nth term of the Fibonacci Sequence,\n斐波那契数列第n项,\nn = "))
    print("F_{}".format(n)," = ",expand((((1+sqrt(5))/2)**n-((1-sqrt(5))/2)**n)/sqrt(5)))

    # 判断是否退出
    reply = input("计算下一个数或退出？(Y\\N)\n")
    while reply not in "Yy":
        if reply in "Nn":
                _exit(0)
        else:
                reply = input("请重新输入：计算下一个数或退出？(Y\\N)\n")
    print("\n\n\n\n\n")
else:
    os._exit(0)