from sys import argv
# "argv" argument variable
# 解包
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
x = input("how about some more? ")
print('haha', x)