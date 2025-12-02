# For day 1 of the challenge, we first need to determine how many times
# a dial points directly at zero in a series of rotations. Then for part
# 2 we need to figure out how many times the dial crosses zero. The input is
# provided in a text file and has a series of instructions. The dial
# starts pointing at 50. Each instruction starts with either L or R
# indicating the direction of rotation, followed by a number indicating
# how many positions to rotate. The range of the dial is from 0 to 99.

# Part 1: Count how many times the dial points directly at zero after
# completing each instruction.
def part1():
    startPosition = 50
    currentPosition = startPosition
    countZeros = 0

    with open("input.txt", 'r') as file:
        for line in file:
            line = line.strip()

            if line[0] == 'L':
                steps = int(line[1::])
                for i in range(steps):
                    currentPosition -= 1
                    if currentPosition < 0:
                        currentPosition = 99
                    if currentPosition == 0 and i == steps - 1:
                        countZeros += 1
            elif line[0] == 'R':
                steps = int(line[1::])
                for i in range(steps):
                    currentPosition += 1
                    if currentPosition > 99:
                        currentPosition = 0
                    if currentPosition == 0 and i == steps - 1:
                        countZeros += 1

    print(countZeros)


# Part 2: Count how many times the dial crosses zero during the entire
# series of instructions.
def part2():
    startPosition = 50
    currentPosition = startPosition
    countZeros = 0

    with open("input.txt", 'r') as file:
        for line in file:
            line = line.strip()

            if line[0] == 'L':
                steps = int(line[1::])
                for i in range(steps):
                    currentPosition -= 1
                    if currentPosition < 0:
                        currentPosition = 99
                    if currentPosition == 0:
                        countZeros += 1
            elif line[0] == 'R':
                steps = int(line[1::])
                for i in range(steps):
                    currentPosition += 1
                    if currentPosition > 99:
                        currentPosition = 0
                    if currentPosition == 0:
                        countZeros += 1

    print(countZeros)


part1()
part2()
