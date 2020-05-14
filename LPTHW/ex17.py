from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# tmp_file = open(from_file)
# tmp_data = tmp_file.read()
x = open(from_file).read()

print(f"The input file is {len(x)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, Ctrl-C to abort.")
input()

y = open(to_file, 'w')
print("----> ", repr(y))
y.write(x)

print("Alright, all done.")
print("abc\rddd")

y.close()