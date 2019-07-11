from model import *
from prior import *

model1 = Model(2,2)
prior1 = Prior(3,[1/6, 2/6, 3/6], [0.1,0.2, 0.3])
posterior1 = prior1.f(0.1) * model1.f_y_given_theta(0.1) / sum()

