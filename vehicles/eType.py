from vehicle import Vehicle

class EType(Vehicle):
    def __init__(self, color, maxOccupants=2):
        super().__init__(color, maxOccupants)
        self.isMostBeautiful = True

    def drive(self):
        if self.isMostBeautiful:
            print(f'You are driving a gorgeous {self.color} car.')
        else:
            print(f'You are objectively wrong.')