from vehicles import Batmobile, Corvette, EType, Mustang, Porsche

new_porsche = Porsche("black")
new_batmobile = Batmobile()
new_corvette = Corvette("red")
new_mustang = Mustang("blue")
new_eType = EType("british racing green")

new_porsche.drive()
print('')
new_batmobile.stop()
print('')
new_mustang.turn("left")