from vehicle import Vehicle

class Porsche(Vehicle):
    def __init__(self, color, maxOccupants=3):
        super().__init__(color, maxOccupants)
        self.engineCooling = "air-cooled"

    def drive(self):
        print(f'The {self.engineCooling} engine in this {self.color} Porsche is an engineering marvel.')