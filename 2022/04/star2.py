def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def func1():
    #todo
    return 0

def func2():
    #todo
    return 0

def main(file_name):
    #todo
    return 0



test1_result = func1('?')
test1_expected_result = 0
if test1_result != test1_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test1_expected_result}, got: {test1_result}")

test2_result = func1('?')
test2_expected_result = 0
if test2_result != test2_expected_result:
    raise Exception(f"TEST_2 FAILED: Expected value: {test2_expected_result}, got: {test2_result}")

test3_result = func2('?')
test3_expected_result = '?'
if test3_result != test3_expected_result:
    raise Exception(f"TEST_3 FAILED: Expected value: {test3_expected_result}, got: {test3_result}")

test4_result = func2('?')
test4_expected_result = '?'
if test3_result != test3_expected_result:
    raise Exception(f"TEST_4 FAILED: Expected value: {test4_expected_result}, got: {test4_result}")

test_result = main("input_test")
expected_result = 0
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {main('input')}")