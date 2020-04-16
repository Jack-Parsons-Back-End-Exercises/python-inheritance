from vehicle import Vehicle

class Corvette(Vehicle):
    def __init__(self, color, maxOccupants=2):
        super().__init__(color, maxOccupants)
        self.topSpeed = 185

    def drive(self):
        print(f'This {self.color} Corvette can reach speeds of {self.topSpeed} miles per hour. Be careful!')