inputFile = open('input', 'r')
lines = inputFile.readlines()
inputFile.close()

def find_trees(inputLines, slope_x, slope_y) :
    trees_found   = 0
    current_x    = 0
    current_y    = 0
    readed_lines = 0
    for line in lines:
        readed_lines += 1

        if readed_lines == 1:
            continue

        current_y    += 1
        if current_y != slope_y:
            continue

        current_x = (current_x + slope_x) % (len(line) - 1)

        if line[current_x] == "#" :
            trees_found += 1
        current_y = 0

    return trees_found

print(find_trees(lines,3,1))
