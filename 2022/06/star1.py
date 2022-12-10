def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def detects_start_of_packet_marker(text):
    # TODO
    return 0

def get_total(file_name):
    total = 0
    
    input_file = open(file_name, 'r')
    for line in input_file:
        total += detects_start_of_packet_marker(line.strip())
    input_file.close()

    return total


### TESTS

test_result = detects_start_of_packet_marker('bvwbjplbgvbhsrlpgdmjqwftvncz')
test_expected_result = 5
if test_result != test_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test_expected_result}, got: {test_result}")

test_result = detects_start_of_packet_marker('nppdvjthqldpwncqszvftbrmjlhg')
test_expected_result = 6
if test_result != test_expected_result:
    raise Exception(f"TEST_2 FAILED: Expected value: {test_expected_result}, got: {test_result}")

test_result = detects_start_of_packet_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
test_expected_result = 10
if test_result != test_expected_result:
    raise Exception(f"TEST_3 FAILED: Expected value: {test_expected_result}, got: {test_result}")

test_result = detects_start_of_packet_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
test_expected_result = 11
if test_result != test_expected_result:
    raise Exception(f"TEST_4 FAILED: Expected value: {test_expected_result}, got: {test_result}")


test_result = get_total("input_test")
expected_result = 2
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_total('input')}")
