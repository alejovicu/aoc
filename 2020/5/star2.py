inputFile = open('input', 'r')
lines = inputFile.readlines()
inputFile.close()

def get_row(borading_pass) :
    row_binary = borading_pass.replace('F','0').replace('B','1')[0:-3]
    return int(row_binary,2)

def get_column(borading_pass) :
    col_binary = borading_pass.replace('L','0').replace('R','1')[-3:len(borading_pass)]
    return int(col_binary,2)

def get_seat_id(row, column) :
    return 8*row + column

def find_seat_id(inputLines) :
    boarding_passes  = []
    for line in lines:
        boarding_pass = line.strip()
        row = get_row(boarding_pass)
        col = get_column(boarding_pass)
        seat_id = get_seat_id(row, col)
        boarding_passes.append(seat_id)
        boarding_passes.sort()

    for i in range(len(boarding_passes)-1):
        if boarding_passes[i] + 1 != boarding_passes[i+1] :
            return boarding_passes[i] + 1
    return -1

print(find_seat_id(lines))
