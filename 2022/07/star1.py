from anytree import Node, RenderTree

def debug(log_message):
    import datetime;
    # debug_enabled = False
    debug_enabled = True
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def get_directories_under_path(current_path):
    return [directory.name for directory in list(filter(lambda node: node.type == 'dir', [children for children in current_path.children]))]

def get_directiory_size(current_path):
    # TODO do it recursively
    return  sum([file.size for file in list(filter(lambda node: node.type == 'file', [children for children in current_path.children]))])

def process_cd(path, fs_tree, current_path, last_line_proccesed):
    if path == '/' :
        current_path = fs_tree['/']
    else:
        if path in get_directories_under_path(current_path):
            current_path = fs_tree[path]
        else:
            fs_tree[path] = Node(path, parent = fs_tree[current_path], type='dir')
            current_path = fs_tree[path]

    last_line_proccesed = last_line_proccesed + 1
    return fs_tree, current_path, last_line_proccesed

def process_ls(console_output, fs_tree, current_path,last_line_proccesed):
    last_line_proccesed = last_line_proccesed + 1
    while console_output[last_line_proccesed][0] != '$':
        debug(console_output[last_line_proccesed])
        if console_output[last_line_proccesed][0] == 'dir' :
            # TODO get list of directories under current path
            if console_output[last_line_proccesed][1] not in fs_tree:
                fs_tree[console_output[last_line_proccesed][1]]
            else:
                fs_tree[path] = Node(path, parent = fs_tree[current_path], type='dir')
                current_path = fs_tree[path]
        last_line_proccesed = last_line_proccesed + 1
    return fs_tree, last_line_proccesed

def process_command(console_output, last_line_proccesed, file_system_tree, current_path):
    # TODO
    debug(console_output[last_line_proccesed])
    if console_output[last_line_proccesed][0] == '$':
        if console_output[last_line_proccesed][1] == 'cd':
            file_system_tree, current_path, last_line_proccesed = process_cd(
                console_output[last_line_proccesed][2],
                file_system_tree,
                current_path,
                last_line_proccesed)
        if console_output[last_line_proccesed][1] == 'ls':
            file_system_tree, last_line_proccesed = process_ls(
                console_output,
                file_system_tree,
                current_path,
                last_line_proccesed)

    return last_line_proccesed, file_system_tree, current_path

def get_file_system(console_output):
    file_system_tree = {}
    root = Node('/', type='dir')
    file_system_tree[root.name] = root
    current_path = file_system_tree[root.name]
    last_line_proccesed = 0

    while last_line_proccesed < len(console_output):
        last_line_proccesed, file_system_tree, current_path = process_command(
            console_output,
            last_line_proccesed,
            file_system_tree,
            current_path)
    
    return file_system_tree

def get_total(file_name):
    total = 0


    console_output_arr=[]
    input_file = open(file_name, 'r')
    for line in input_file:
        console_output_arr.append(line.strip().split(' '))
    input_file.close()

    file_system_tree = get_file_system(console_output_arr)

    return total

### TESTS
test_root = Node('/', type='dir')
test_path1 = Node('a', type='dir', parent = test_root)
test_path2 = Node('b', type='dir', parent = test_root)
test_file1 = Node('a_file.txt', type='file', parent = test_root, size=1234)
test_result = get_directories_under_path(test_root)
test_expected_result = ['a', 'b']
if test_result != test_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test_expected_result}, got: {test_result}")

test_root = Node('/', type='dir')
test_path1 = Node('a', type='dir', parent = test_root)
test_path2 = Node('b', type='dir', parent = test_root)
test_file1 = Node('a_file.txt', type='file', parent = test_root, size=1000)
test_file2 = Node('a_file.txt', type='file', parent = test_root, size=300)
test_result = get_directiory_size(test_root)
test_expected_result = 1300
if test_result != test_expected_result:
    raise Exception(f"TEST_2 FAILED: Expected value: {test_expected_result}, got: {test_result}")

# test_result = get_total("input_test")
# expected_result = 2
# if test_result != expected_result:
#     raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

# print(f"Result: {get_total('input')}")
