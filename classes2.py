from space.planet import Planet
from space.calc import planet_vol, planet_mass

naboo = Planet('Tierra', 300000, 8, 'Solar system')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(naboo_mass)
print(naboo_vol)