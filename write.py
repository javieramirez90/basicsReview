with open('files/write.txt', 'w') as write_file: #the second argument of the open method allows us to write in the file
  write_file.write('Hello world')
  

with open('files/write.txt', 'a') as write_file: #the second argument of the open method allows us to write after the last line we wrote
   write_file.write('\nHello world for a copy of the second line')


quotes = [
  '\nI can resist everything except temptation',
  '\nWe are all in the gutter, but some of us are looking at the stars',
  '\nAlways forgive your enemies -  nothing annoys them so much'
]

with open('files/write.txt', 'a') as write_file:
  write_file.writelines(quotes)