

from Car import *

class Hybrid(Car):

    def __init__ (self, miles, color, charge):
        super().__init__(miles,color)
        self.charge = charge

    def setCharge(self, chargeLevel):
        self.charge = chargeLevel

    def __str__(self):
        return super().__str__() + " and the charge level is: " +str(self.charge)
