class Car:

    def __init__ (self, miles, color):
        self.miles = miles
        self.color = color

    def changeMiles(self, newMiles):
        self.miles = newMiles

    def changeColor(self, newColor):
        self.color = newColor

    def __str__(self):
        return "The miles are: " + str(self.miles) + " and the color is: " + str(self.color)

