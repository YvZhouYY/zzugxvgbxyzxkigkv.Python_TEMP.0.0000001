# -*- coding: UTF-8 -*-
from sympy import sqrt,expand
n = int(input("The Nth term of the Fibonacci Sequence,\n斐波那契数列第n项,\nn = "))
print("F_{}".format(n)," = ",expand((((1+sqrt(5))/2)**n-((1-sqrt(5))/2)**n)/sqrt(5)))