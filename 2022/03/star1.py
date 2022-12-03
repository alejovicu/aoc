def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def get_prio_value(item_type):
    if item_type.islower():
      return ord(item_type) - 96
    else:
      return ord(item_type) - 38

def get_rucksack_prio(rucksack):
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    for char in compartment1:
      if char in compartment2 :
        return char
    return None

def get_prio_sum(file_name):
    total = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            debug(line.strip())
            total = total + get_prio_value(get_rucksack_prio(line.strip()))
    return total



test1_result = get_prio_value('p')
test1_expected_result = 16
if test1_result != test1_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test1_expected_result}, got: {test1_result}")

test2_result = get_prio_value('L')
test2_expected_result = 38
if test2_result != test2_expected_result:
    raise Exception(f"TEST_2 FAILED: Expected value: {test2_expected_result}, got: {test2_result}")

test3_result = get_rucksack_prio('vJrwpWtwJgWrhcsFMMfFFhFp')
test3_expected_result = 'p'
if test3_result != test3_expected_result:
    raise Exception(f"TEST_3 FAILED: Expected value: {test3_expected_result}, got: {test3_result}")

test4_result = get_rucksack_prio('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')
test4_expected_result = 'L'
if test3_result != test3_expected_result:
    raise Exception(f"TEST_4 FAILED: Expected value: {test4_expected_result}, got: {test4_result}")

test_result = get_prio_sum("input_test")
expected_result = 157
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_prio_sum('input')}")