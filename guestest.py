#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import prettytable as pt

'''
也可以输入时不做int判断
时候对输入做type判断
这样可以记录异常输入
'''

if __name__ == '__main__':
    tb = pt.PrettyTable()
    num = random.randint(0, 100)
    sju = num

    tb.field_names = ["猜数字", "结果"]
    tb.add_row(["随机数", str(sju)])

    while True:
        try:
            x = int(input("请输入数字："))
        except ValueError:
            print("输入非数字，请重新输入：")
        else:
            if x < num:
                print("数字小")
                tb.add_row([x, "数字小"])
            elif x > num:
                print("数字大")
                tb.add_row([x, "数字大"])
            else:
                print("Bingou！ 答对了")
                tb.add_row([x, "Bingo！ 答对了"])
                break
    print(tb)
