from random import shuffle

def jumble(word):
  anagram = list(word)
  shuffle(anagram)
  return ''.join(anagram)

words =  ['beetroot', 'carrots', 'potatoes']
anagrams = []

#first way
# for word in words:
#   anagrams.append(jumble(word))
# print(anagrams)

#second way
print(list(map(jumble, words)))

#third way
print([jumble(word) for word in words])