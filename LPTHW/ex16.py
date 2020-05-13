from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, hit Ctrl-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# target_file = open(filename, 'w')
target_file = open(filename, 'r+')

print("Truncating the file. Goodbye!")
# target_file.truncate()

print("Now I'm gonna ask you for 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm gonna write these lines to the file.")

# target_file.write(line1)
# target_file.write('\n')
# target_file.write(line2)
# target_file.write('\n')
# target_file.write(line3)
# target_file.write('\n')
target_file.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target_file.close()
print("If it's closed? ",target_file.closed)
