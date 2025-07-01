import math
pitch = float(input('Belt pitch:\n>'))
teeth = int(input('Sprocket teeth:\n>'))

PD = 5/math.sin(math.radians(15))
OD = PD - (2.4/math.tan(math.radians(360/teeth)))
print('Pitch Diameter:', PD)
print('Outside Diameter:',OD)