import sys

file = open(sys.argv[1], "r")
content = file.read()

memory = []
index = 0

for c in content:
    if memory[index] > 255:
        memory[index] = 0
    elif memory[index] < 0:
        memory[index] = 255