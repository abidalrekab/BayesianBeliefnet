from math import factorial


class Model:

    def __init__(self, N, Y):
        self.N = N
        self.Y = Y

    def f_y_given_theta(self, theta):
        return self.nPr() * pow(theta, self.Y) * pow((1 - theta), (self.N - self.Y))

    def nPr(self):
        return int(factorial(self.N) / factorial(self.N - self.Y))
