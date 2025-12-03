# For day 2, we recieve a single line of comma separated values
# representing product ID ranges. Each range has a firstID and a
# last ID separated by a hyphen. We need to determine if any
# IDs within the range are strictly made of a sequence of repeated digits.
# Like (11, 2424, 123123). If an ID has a sequence of repeated
# digits, it is considered invalid. For part 1, we get the answer
# by summing all invalid IDs. For part 2, an ID is invalid if there
# are any number of repeated sequences of digits (111, 121212, 6666666).
# The answer for part 2 is also the sum of all invalid IDs.


def part1():

    def hasRepeat(number: int) -> bool:
        id = str(number)
        length = len(id)
        maxSeqLength = length // 2

        if length % 2 != 0 or int(id[0]) == 0:
            return False

        if id[0:maxSeqLength] == id[maxSeqLength:length + 1]:
            return True

    sum = 0

    with open("input.txt", 'r') as file:
        ids = file.readline().strip().split(',')

        for id in ids:
            first, second = id.split('-')
            for i in range(int(first), int(second) + 1):
                if hasRepeat(i):
                    sum += i
    print(sum)


def part2():

    def hasRepeat(number: int) -> bool:
        id = str(number)
        length = len(id)
        maxSeqLength = length // 2

        if int(id[0]) == 0:
            return False

        for seqLength in range(1, maxSeqLength + 1):
            if length % seqLength == 0:
                sequence = id[0:seqLength]
                repeated = sequence * (length // seqLength)
                if repeated == id:
                    return True

    sum = 0

    with open("input.txt", 'r') as file:
        ids = file.readline().strip().split(',')

        for id in ids:
            first, second = id.split('-')
            for i in range(int(first), int(second) + 1):
                if hasRepeat(i):
                    sum += i
    print(sum)


part1()
part2()
