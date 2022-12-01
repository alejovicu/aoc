def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def getMaxCalories(file_name):
    max_value = 0
    current = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            debug(line.strip())
            if(line == "\n"):
                if current > max_value:
                    max_value = current
                    debug(f"max: {max_value}")
                current = 0
            else:
                current = current + int(line)
                debug(f"current: {current}")
                debug(f"max: {max_value}")
    return max_value

test_result = getMaxCalories("test_input")
expected_result = 24000
if test_result != expected_result:
    raise Exception(f"TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {getMaxCalories('input')}")