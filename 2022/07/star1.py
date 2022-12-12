def debug(log_message):
    import datetime;
    # debug_enabled = False
    debug_enabled = True
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def get_directiory_size(fs_tree, command):
    # TODO
    return 0

def process_cd(fs_tree, command):
    # TODO
    return 0

def process_ls(fs_tree, command):
    # TODO
    return 0

def process_command(fs_tree, current_path, command_arr):
    # TODO
    return 0

def get_total(file_name):
    total = 0

    file_system_tree = None
    current_path = None
    input_file = open(file_name, 'r')
    for line in input_file:
        line_arr = line.strip().split(' ')
        debug(line_arr)
        # total += get_directiory_size(line.strip())
    input_file.close()

    return total

### TESTS

# test1_result = f2('test_value')
# test1_expected_result = True
# if test1_result != test1_expected_result:
#     raise Exception(f"TEST_1 FAILED: Expected value: {test1_expected_result}, got: {test1_result}")

# test2_result = f2('test_value')
# test2_expected_result = True
# if test2_result != test2_expected_result:
#     raise Exception(f"TEST_2 FAILED: Expected value: {test2_expected_result}, got: {test2_result}")

test_result = get_total("input_test")
expected_result = 2
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

# print(f"Result: {get_total('input')}")
