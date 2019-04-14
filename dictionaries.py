# ninja_belts = {
#   'Dany': 'red',
#   'Javier': 'black',
#   'Ariel': 'white'
# }

# # print(ninja_belts['Javier'])

# # print('yoshi' in ninja_belts)

# # print(ninja_belts.keys())

# # lista = list(ninja_belts.keys())

# # print(lista)

# # print(ninja_belts.values())

# # values = list(ninja_belts.values())
# # print(values.count('red'))

# # print(values)
# # print('El primero', ninja_belts)

# # ninja_belts['Carlos'] = 'yellow'

# # print('El segundo', ninja_belts)

# person = dict(name='Xavier', age=28, profession="Developer")

# print(person)
# def ninja_intro(dictionary):
#   for key,val in dictionary.items():
#     print(f'I am {key} and I am a {val} belt')

def belt_count(dictionary):

  belts = list(dictionary.values())
  for belt in set(belts):
    num = belts.count(belt)
    print(f'the are {num} {belt} belts')

ninja_belts = { }

while True:
  ninja_name =  input('Enter a ninja name: ')
  ninja_belt =  input('Enter a belt color: ')
  ninja_belts[ninja_name] = ninja_belt

  another = input('add another? (y/n) ')
  if another == 'y':
    continue
  else:
    break

#ninja_intro(ninja_belts)
belt_count(ninja_belts)