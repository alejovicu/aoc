inputFile = open('input', 'r')
lines = inputFile.readlines()
inputFile.close()

def validate_passport(passport_arr) :
    req_cond = {
        "byr" : False,
        "iyr" : False,
        "eyr" : False,
        "hgt" : False,
        "hcl" : False,
        "ecl" : False,
        "pid" : False
    }

    for field in passport_arr :
        condition = field.split(":")[0]
        if condition in req_cond :
            req_cond[condition] = True

    for condition in req_cond:
        if not req_cond[condition] :
            return False
    return True

def find_valid_passports(inputLines) :
    vp_found   = 0
    passport_str = ""
    for line in lines:
        if len(line) == 1 :
            if validate_passport(passport_str.replace("\n"," ").strip().split(" ")) :
                vp_found  += 1
            passport_str = ""
        else :
            passport_str = passport_str + line
    return vp_found

print(find_valid_passports(lines))
