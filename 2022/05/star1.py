def debug(log_message):
    import datetime;
    debug_enabled = True
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def create_stack_from_line(line):
    stack_matrix = []
    for line in stack:
        count = 1
        for i in range(len(line)):
            if i == count:
                stack_matrixline[i]
    print(stack_matrix)
    return stack

def cleanup_stack(stack):
    stack_matrix = []
    for line in stack:
        count = 1
        for i in range(len(line)):
            if i == count:
                stack_matrixline[i]
    print(stack_matrix)
    return stack

def f2(line):
    # TODO
    return 0

def get_total(file_name):
    total = 0
    stack = []
    actions = []
    is_stack = True
    input_file = open(file_name, 'r')
    for line in input_file:
        ls = line.strip()
        if ls == '' :
            is_stack = False
            stack.pop()
            continue
        
        if is_stack :
            stack.append(line.replace("\n", ""))
        else :
            actions.append(ls)
        total += f2(ls)
    input_file.close()
    debug(stack)
    debug(actions)
    return total

### TESTS

test1_result = cleanup_stack([
    '    [D]    ',
    '[N] [C]    ',
    '[Z] [M] [P]'
])
test1_expected_result = [
    ['N','Z'],
    ['D','C','M'],
    ['P']
]
if test1_result != test1_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test1_expected_result}, got: {test1_result}")

# test2_result = f2('test_value')
# test2_expected_result = True
# if test2_result != test2_expected_result:
#     raise Exception(f"TEST_2 FAILED: Expected value: {test2_expected_result}, got: {test2_result}")

test_result = get_total("input_test")
expected_result = 2
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_total('input')}")
