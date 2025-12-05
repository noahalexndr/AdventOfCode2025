# Day 4 challenge

def part1():
    grid = []
    total = 0

    with open("input.txt", 'r') as file:
        for line in file:
            grid.append(list(line.strip()))

        rowCount = len(grid)
        colCount = len(grid[0])
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in range(rowCount):
            for j in range(colCount):
                adjacent = 0
                if grid[i][j] == '@':
                    for d in range(8):
                        ni = i + dr[d]
                        nj = j + dc[d]
                        if 0 <= ni < rowCount and 0 <= nj < colCount:
                            if grid[ni][nj] == '@':
                                adjacent += 1
                    if adjacent < 4:
                        total += 1

        print(f"Part 1 Final Total: {total}")


def part2():
    grid = []
    total = 0

    with open("input.txt", 'r') as file:
        for line in file:
            grid.append(list(line.strip()))

        rowCount = len(grid)
        colCount = len(grid[0])
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        def removePaper():
            xyRemoved = []
            count = 0

            for i in range(rowCount):
                for j in range(colCount):
                    adjacent = 0
                    if grid[i][j] == '@':
                        for d in range(8):
                            ni = i + dr[d]
                            nj = j + dc[d]
                            if 0 <= ni < rowCount and 0 <= nj < colCount:
                                if grid[ni][nj] == '@':
                                    adjacent += 1
                        if adjacent < 4:
                            count += 1
                            xyRemoved.append((i, j))

            for x, y in xyRemoved:
                grid[x][y] = '.'

            xyRemoved.clear()

            return count

        while True:
            removed = removePaper()
            if removed == 0:
                break
            total += removed
        print(f"Part 2 Final Total: {total}")


part1()
part2()
