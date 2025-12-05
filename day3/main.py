# Day 3 challenge

def part1():
    totalJoltage = 0

    with open("input.txt", 'r') as file:
        for line in file:
            bank = line.strip()
            batteries = [0, 0]

            for i in range(len(bank)):
                if int(bank[i]) > batteries[0] and i < len(bank) - 1:
                    batteries[0] = int(bank[i])
                    batteries[1] = int(bank[i + 1])
                elif int(bank[i]) > batteries[1]:
                    batteries[1] = int(bank[i])
            totalJoltage += int(str(batteries[0]) + str(batteries[1]))
    print(totalJoltage)


def part2():
    totalJoltage = 0

    with open("input.txt", 'r') as file:
        for line in file:
            bank = line.strip()
            remaining = 12
            currentPosition = 0
            maxJoltage = ""

            while remaining > 0:

                window = bank[currentPosition:len(bank) - remaining + 1]

                for i in range(9, 0, -1):
                    if window.find(str(i)) >= 0:
                        maxJoltage += str(i)
                        currentPosition += window.find(str(i)) + 1
                        remaining -= 1
                        break
            totalJoltage += int(maxJoltage)
        print(totalJoltage)


part1()
part2()
