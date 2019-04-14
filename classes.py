class Planet:
  #class level attributes
  shape = 'round'

  def __init__(self, name, radius, system):
    #instance attributes
    self.name = name
    self.radius = radius
    self.gravity = 5.5
    self.system = system
  
  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'
    
  @classmethod
  def commmons(cls):
    return f'All planets are {cls. shape}'

  @staticmethod
  def spin(speed ='2000 miles per hour'):
    return f'The planets spins {speed}'

hoth =  Planet('Huth', 300000, 'Hoth System')

# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(hoth.orbit())


# print(hoth.shape)
