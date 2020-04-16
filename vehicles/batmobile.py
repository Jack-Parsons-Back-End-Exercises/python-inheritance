from vehicle import Vehicle

class Batmobile(Vehicle):
    def __init__(self, color="black", maxOccupants=1):
        super().__init__(color, maxOccupants)
        self.weapons = {"Caltrops", "Oil Slick"}

    def drive(self):
        print(f'The {self.color} Batmobile roars to life. I am the night.')

    def stop(self):
        print('Evil does not stop, so neither does the Batmobile.')