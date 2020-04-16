from vehicle import Vehicle

class Mustang(Vehicle):
    def __init__(self, color, maxOccupants=4):
        super().__init__(color, maxOccupants)
        self.famousDriver = "Steve McQueen"

    def drive(self):
        print(f'Be like {self.famousDriver} and let this {self.color} Mustang gallop!')

    def turn(self, direction):
        print("Yeah, this isn't really a turning car...")