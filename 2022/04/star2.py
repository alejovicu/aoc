def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def get_elf_section(elf):
    range_pair=elf.strip().split("-")
    return set(range(int(range_pair[0]),int(range_pair[1])+1))

def are_sections_overlapped(elf1, elf2):
    section1=get_elf_section(elf1)
    section2=get_elf_section(elf2)
    len_both_sections =len(section1) + len(section2)
    len_both_sections_joined = len(section1.union(section2))
    debug(f"len_both_sections:{len_both_sections} | len_both_sections_joined: {len_both_sections_joined}")
    #If lenght differs it's because there were duplicated items and were removed in the union
    return len_both_sections != len_both_sections_joined

def get_total(file_name):
    total = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            elf_pair=line.strip().split(",")
            total += 1 if are_sections_overlapped(elf_pair[0],elf_pair[1]) else 0
    return total

### TESTS

test1_result = are_sections_overlapped('5-7','7-9')
test1_expected_result = True
if test1_result != test1_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test1_expected_result}, got: {test1_result}")

test2_result = are_sections_overlapped('2-8','3-7')
test2_expected_result = True
if test2_result != test2_expected_result:
    raise Exception(f"TEST_2 FAILED: Expected value: {test2_expected_result}, got: {test2_result}")

test3_result = are_sections_overlapped('2-4','6-8')
test3_expected_result = False
if test3_result != test3_expected_result:
    raise Exception(f"TEST_3 FAILED: Expected value: {test3_expected_result}, got: {test3_result}")

test_result = get_total("input_test")
expected_result = 4
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_total('input')}")
