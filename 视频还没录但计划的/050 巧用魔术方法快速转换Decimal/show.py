"""
by shikukuya
"""

from decimal import Decimal
from typing import Union


class Decimaler:
    # 用 Decimaler() @ "value" 初始化

    def __matmul__(self, other: Union[str, "Decimaler"]):
        if isinstance(other, str):
            self.value = Decimal(other)
        else:
            self.value = other.value
        return self

    # 实现各种运算符

    def __add__(self, other: str):
        self.value += Decimal(other)
        return self

    def __sub__(self, other: str):
        self.value -= Decimal(other)
        return self

    def __mul__(self, other: str):
        self.value *= Decimal(other)
        return self

    def __truediv__(self, other: str):
        self.value /= Decimal(other)
        return self

    def __pow__(self, other: str):
        self.value **= Decimal(other)
        return self

    # 转换为原生类型

    def __repr__(self):
        return str(self.value)

    def __float__(self):
        return float(self.value)


o = Decimaler()


print((0.1 + 0.2) / 0.1 * 10)
print((o @ "0.1" + "0.2") / "0.1" * "10")
