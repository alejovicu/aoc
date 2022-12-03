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

def get_rucksack_prio(rucksack1, rucksack2, rucksack3):
    debug(f"{rucksack1}\n{rucksack2}\n{rucksack3}")
    for r1_char in rucksack1:
      if r1_char in rucksack2:
        if r1_char in rucksack3:
          debug(f"group_prio: {r1_char}")
          return r1_char
    return None

def get_prio_sum(file_name):
    total = 0
    rucksack_group = []
    with open(file_name) as f:
        for index, line in enumerate(f):
            rucksack_group.append(line.strip())
            if len(rucksack_group) == 3:
                total = total + get_prio_value( get_rucksack_prio(rucksack_group[0],
                  rucksack_group[1],
                  rucksack_group[2]))
                rucksack_group.clear()
    return total



test1_result = get_prio_value('r')
test1_expected_result = 18
if test1_result != test1_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test1_expected_result}, got: {test1_result}")

test2_result = get_prio_value('Z')
test2_expected_result = 52
if test2_result != test2_expected_result:
    raise Exception(f"TEST_2 FAILED: Expected value: {test2_expected_result}, got: {test2_result}")

test3_result = get_rucksack_prio('vJrwpWtwJgWrhcsFMMfFFhFp',
  'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
  'PmmdzqPrVvPwwTWBwg')
test3_expected_result = 'r'
if test3_result != test3_expected_result:
    raise Exception(f"TEST_3 FAILED: Expected value: {test3_expected_result}, got: {test3_result}")

test4_result = get_rucksack_prio('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
  'ttgJtRGJQctTZtZT',
  'CrZsJsPPZsGzwwsLwLmpwMDw')
test4_expected_result = 'Z'
if test3_result != test3_expected_result:
    raise Exception(f"TEST_4 FAILED: Expected value: {test4_expected_result}, got: {test4_result}")

test_result = get_prio_sum("input_test")
expected_result = 70
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_prio_sum('input')}")