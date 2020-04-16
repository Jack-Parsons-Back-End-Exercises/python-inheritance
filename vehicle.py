class Vehicle:

    def __init__(self, color, maxOccupants):
        self.color = color
        self.maxOccupants = maxOccupants

    def drive(self):
        pass

    def turn(self, direction):
        print(f'You turned the car {direction}')

    def stop(self):
        print(f'You have stopped the car.')