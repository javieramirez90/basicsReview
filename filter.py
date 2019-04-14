grades = ['A', 'B', 'F', 'C', 'F', 'A']

def remove_fails(grade):
  return grade != 'F'

# first way using less lines of code
print(list(filter(remove_fails, grades)))

filtered_grades = []

#second way using for loop

for grade in grades:
  if(grade != 'F'):
    filtered_grades.append(grade)

print(filtered_grades)

#third way using comprehension
print([grade for grade in grades if grade != 'F'])