from sys import argv

script, filename = argv
print(f"This is your file: {filename}")
# x = open(filename, 'w+')
x = open(filename, 'r+')
x.write('WASP')
# print(x.read(), end='')