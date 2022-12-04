inputFile = open('input', 'r')
lines = inputFile.readlines()
inputFile.close()

def get_gropup_answers(inputLines) :
    found   = 0
    readed  = 0

    group_size = 0
    answer_group_str = ""
    for line in lines:
        if line == "\n" or len(lines) == readed :
            leters_found = "".join(dict.fromkeys(answer_group_str))
            for leter in leters_found :
                if answer_group_str.count(leter) == group_size :
                    found += 1
            answer_group_str = ""
            group_size =0
        else :
            answer_group_str = answer_group_str + line.replace("\n"," ").strip()
            group_size +=1
        readed += 1
    return found

print(get_gropup_answers(lines))
