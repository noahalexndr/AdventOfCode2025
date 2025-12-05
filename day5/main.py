# Day 5 challenges

def part1():
    ranges = []
    ids = []
    cleanSections = []
    total = 0
    with open("input.txt", 'r') as file:
        sections = file.read().strip().split("\n\n")

        for section in sections:
            cleanSections.append(section.split("\n"))

        ranges = cleanSections[0]
        ids = cleanSections[1]
        ids = [int(i) for i in ids]

        for id in ids:
            for r in ranges:
                start, end = r.split("-")
                start, end = int(start), int(end)
                if id >= start and id <= end:
                    total += 1
                    break
    print(total)


def part2():
    ranges = []
    newRanges = []
    total = 0

    def merge_ranges(ranges):
        if not ranges:
            return []

        ranges.sort(key=lambda x: x[0])

        merged = [ranges[0]]

        for currentStart, currentEnd in ranges[1:]:
            lastStart, lastEnd = merged[-1]
            if currentStart <= lastEnd:
                merged[-1][1] = max(lastEnd, currentEnd)
            else:
                merged.append([currentStart, currentEnd])

        return merged

    with open("input.txt", 'r') as file:
        for line in file:
            if line.strip() == "":
                break
            else:
                ranges.append(line.strip())
        for r in ranges:
            start, end = r.split("-")
            start, end = int(start), int(end)

            newRanges.append([start, end])

        mergedRanges = merge_ranges(newRanges)

        for r in mergedRanges:
            total += r[1] - r[0] + 1
    print(total)


part1()
part2()
