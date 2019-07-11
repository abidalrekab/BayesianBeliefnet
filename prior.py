# This module to calculate the prior distribution
class Prior:

    def __init__(self, num_val, probs = None, vals = None) :
        self.num_val = num_val
        self.probs = probs
        self.vals = vals

    def f(self, theta):
        return self.vals[self.probs.index(theta)]





