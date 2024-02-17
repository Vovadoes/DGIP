import math

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
        for i in range(k1, k2 + 1):
            self.summ_p_n += self.p_n(i)

    def p_n(self, k):
        l = 1  # !!!
        return pow(math.e, l) * pow(l, k) / math.factorial(k)


if __name__ == "__main__":
    n = 200
    p = 0.002
    k1 = 1
    k2 = 5
    calculation = Calculation(n, p, k1, k2)
    print(calculation.summ_p_n)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
