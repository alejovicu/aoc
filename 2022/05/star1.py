from collections import deque

def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def process_stack_lines(stack_str):
    tmp_matrix = []
    queue_matrix = []
    for line in stack_str:
        tmp_matrix.append( [line[x] for x in range(1,len(line), 4)] )
    debug(f"tmp_matrix: {tmp_matrix}")

    for i in range(len(tmp_matrix[0])):
        tmp_list = [row[i] for row in tmp_matrix]
        queue_matrix.append(list(filter(lambda item: item != ' ', tmp_list)))
    debug(f"queue_matrix: {queue_matrix}")
    return queue_matrix

def process_action(stack, quantity, source_queue, destination_queue):
    debug(f"stack before: {stack}")
    sq = deque(stack[source_queue-1])
    dq = deque(stack[destination_queue-1])
    for item in range(quantity):
        dq.appendleft(sq.popleft())
    stack[source_queue-1] = list(sq)
    stack[destination_queue-1] = list(dq)
    debug(f"stack after: {stack}")
    return stack

def process_action_lines(stack, actions_str):
    
    for action in actions_str:
        tmp_action_list=action.split(" ")
        debug(tmp_action_list)
        stack = process_action(stack,
            int(tmp_action_list[1]), #quantity
            int(tmp_action_list[3]), #source_queue
            int(tmp_action_list[5])) #destination_queue
    return stack

def get_total(file_name):
    stack_str = []
    actions_str = []
    is_stack = True
    input_file = open(file_name, 'r')
    for line in input_file:
        ls = line.strip()
        if ls == '' :
            is_stack = False
            stack_str.pop()
            continue
        
        if is_stack :
            stack_str.append(line.replace("\n", ""))
        else :
            actions_str.append(ls)
    input_file.close()
    stack = process_stack_lines(stack_str)
    ordered_stack = process_action_lines(stack, actions_str)
    debug(stack_str)
    debug(actions_str)
    debug(ordered_stack)
    result = ""
    for queue in ordered_stack:
        result = f"{result}{queue[0]}"
    return result

### TESTS

test1_result = process_stack_lines([
    '    [D]    ',
    '[N] [C]    ',
    '[Z] [M] [P]'
])
test1_expected_result = [
    ['N', 'Z'],
    ['D', 'C', 'M'],
    ['P']]
if test1_result != test1_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test1_expected_result}, got: {test1_result}")

test2_result = process_action(
    [
    ['N', 'Z'],
    ['D', 'C', 'M'],
    ['P']],
    1,
    2,
    3
    )
test2_expected_result = [
    ['N', 'Z'],
    ['C', 'M'],
    ['D','P']]
if test2_result != test2_expected_result:
    raise Exception(f"TEST_2 FAILED: Expected value: {test2_expected_result}, got: {test2_result}")

test_result = get_total("input_test")
expected_result = 'CMZ'
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_total('input')}")
