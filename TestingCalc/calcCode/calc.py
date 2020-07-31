# !usr/bin/env python
# -*- coding:utf-8 _*-


class Calculator:
    def add(self, a, b):
        """加法"""
        try:
            res = a + b
        except Exception as e:
            return "请输入合法数据"
        else:
            return res

    def sub(self, a, b):
        """减法"""
        try:
            res = a - b
        except Exception as e:
            return "请输入合法数据"
        else:
            return res

    def multi(self, a, b):
        """乘法"""
        try:
            res = a * b
        except Exception as e:
            return "请输入合法参数"
        else:
            return res

    def div(self, a, b):
        """除法"""
        try:
            res = a / b
        except ZeroDivisionError as e:
            return "除数不能为0"
        except TypeError as e:
            return "请输入合法参数"
        else:
            return res


if __name__ == '__main__':
    print(Calculator().multi("1", 2))
