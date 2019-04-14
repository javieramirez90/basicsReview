# def greet():
#     print('Hello mutherfucker')
#
# greet()

# def saludo(nombre, tiempo):
#   print(f'Good{tiempo}{nombre}')

# name = input('Enter your name: ')
# time = input('Enter the time of  the day: ')

# saludo(name, time)

def area(radius):
  a = 3.1416 * radius ** 2
  # print(f'The area of your circle is {a}')
  return a

def vol(area, length):
  print(area * length)

r = int(input('Gimme the radius of your circle: '))
length = int(input('Enter a length: '))

area_calc = area(r)
vol(area_calc, length)

