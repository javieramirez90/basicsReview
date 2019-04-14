nums = [1,2,3,4,5,6]

def square(n):
  return n * n

# print(list(map(square,nums)))

#lambda
# lambda n: n * n

print(list(map(lambda n: n ** 3,nums)))