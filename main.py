import math
from decimal import Decimal

# from Charts import *

# from scipy.stats import t

# CONST
pi = 3.14159265
Yc = 17.3 * (10 ** -6)


class Calculation:
    def __init__(self, n, p, k1, k2):
        # q = 1 - p
        # if (n * p - q) == int(n * p - q):
        #     self.k = int(n * p - q)
        # else:
        #     self.k = math.ceil(n * p - q)
        self.summ_p_n = 0
        self.n = n
        self.p = p
        for i in range(k1, k2 + 1):
            self.summ_p_n += self.p_n(i)
            print(self.p_n(i))

    def p_n(self, k):
        l = self.n * self.p  # !!!
        return Decimal(Decimal(math.e ** (-l)) * Decimal(l ** k) / Decimal(math.factorial(k)))


if __name__ == "__main__":
    n = 800
    p = 0.005
    k1 = 0
    k2 = 3
    calculation = Calculation(n, p, k1, k2)
    print(calculation.summ_p_n)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
