inputFile = open('input', 'r')
lines = inputFile.readlines()
inputFile.close()

slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]
result = 1

def find_trees(inputLines, slope_x, slope_y) :
    trees_found  = 0
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

for slope in slopes:
    result *= find_trees(lines,slope[0],slope[1])
print (result)
