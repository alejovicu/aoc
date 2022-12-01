def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def sort_top3(current, top_3):
    if current > top_3[0]:
        top_3[2] = top_3[1]
        top_3[1] = top_3[0]
        top_3[0] = current
        debug(f"top_3[0]: {top_3[0]}")

    elif current > top_3[1]:
        top_3[2] = top_3[1]
        top_3[1] = current
        debug(f"top_3[1]: {top_3[1]}")
    elif current > top_3[2]:
        top_3[2] = current
        debug(f"top_3[2]: {top_3[2]}")
    return top_3

def getMaxCalories(file_name):
    top_3 = [0,0,0]
    current = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            debug(line.strip())
            if(line == "\n"):
                top_3 = sort_top3(current, top_3)
                current = 0
            else:
                current = current + int(line)
                debug(f"current: {current}")
                debug(f"max: {top_3}")


    top_3 = sort_top3(current, top_3)
    return sum(top_3)

test_result = getMaxCalories("test_input")
expected_result = 45000
if test_result != expected_result:
    raise Exception(f"TEST FAILED: Expected value: {expected_result}, got: {test_result}")


print(f"Result: {getMaxCalories('input')}")