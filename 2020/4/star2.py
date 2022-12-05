import re

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
        cond_val  = field.split(":")[1]

        if condition == "byr" :
            if len(cond_val) == 4 and int(cond_val) >= 1920 and int(cond_val) <= 2002 :
                req_cond[condition] = True
        elif condition == "iyr" :
            if len(cond_val) == 4 and int(cond_val) >= 2010 and int(cond_val) <= 2020 :
                req_cond[condition] = True
        elif condition == "eyr" :
            if len(cond_val) == 4 and int(cond_val) >= 2020 and int(cond_val) <= 2030 :
                req_cond[condition] = True
        elif condition == "hgt" :
            if re.search(r'^([0-9])+([c][m]|[i][n])$', cond_val) :
                unit_type = cond_val[-2:len(cond_val)]
                unit = int(cond_val[0:-2])
                if unit_type == "cm" and unit >=150 and unit <= 193 :
                    req_cond[condition] = True
                if unit_type == "in" and unit >=59 and unit <= 76 :
                    req_cond[condition] = True
        elif condition == "hcl" :
            if re.search(r'^#([0-9|a-f|A-F]){6}$', cond_val) :
                req_cond[condition] = True
        elif condition == "ecl" :
            if cond_val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] :
                req_cond[condition] = True
        elif condition == "pid" :
            if re.search(r'^([0-9]){9}$', cond_val) :
                req_cond[condition] = True
    print(req_cond)
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
