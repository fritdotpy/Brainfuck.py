import sys

with open(sys.argv[1], "r") as file:
    content = file.read()

# print(content)

memory = [0] * 30000
index = 0
loop = False
func = ""

i = 0
while i < len(content):
    instruction = content[i]
    match instruction:
        case ">":
            index += 1
            if index >= 29999:
                index = 0
        case "<":
            index -= 1
            if index < 0:
                index = 29999
        case "-":
            memory[index] -= 1
            if memory[index] < 0:
                memory[index] = 255
        case "+":
            memory[index] += 1
            if memory[index] > 255:
                memory[index] = 0
        case ".":
            print(chr(memory[index]), end="")
        case ",":
            memory[index] = ord(input("")[0])
        case "[":
            if memory[index] == 0:
                depth = 1
                while depth > 0 and i >= 0:
                    i += 1
                    if content[i] == "[":
                        depth += 1
                    elif content[i] == "]":
                        depth -= 1

        case "]":
            if memory[index] != 0:
                depth = 1
                while depth > 0 and i >= 0:
                    i -= 1
                    if content[i] == "]":
                        depth += 1
                    elif content[i] == "[":
                        depth -= 1
    i += 1
