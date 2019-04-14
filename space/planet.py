class Planet:
  
  shape = 'round'
  
  def __init__(self, name, radius, gravity, system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system
    
  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'
  
  @classmethod
  def commmons(cls):
    return f'All planets are {cls. shape}'

  @staticmethod
  def spin(speed ='2000 miles per hour'):
    return f'The planets spins {speed}'
    