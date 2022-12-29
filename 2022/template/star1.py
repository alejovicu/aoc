def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def f1():
    # TODO
    return 0

def f2(line):
    # TODO
    return 0

def get_total(file_name):
    total = 0
    
    input_file = open(file_name, 'r')
    for line in input_file:
        total += f2(line.strip())
    input_file.close()

    return total

### TESTS

test_result = f2('test_value')
test_expected_result = True
if test_result != test_expected_result:
    raise Exception(f"TEST 1 FAILED: Expected value: {test_result}, got: {test_expected_result}")

test_result = f2('test_value')
test_expected_result = True
if test_result != test_expected_result:
    raise Exception(f"TEST 2 FAILED: Expected value: {test_result}, got: {test_expected_result}")

test_result = get_total("input_test")
expected_result = 2
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_total('input')}")
