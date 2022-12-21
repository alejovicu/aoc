from anytree import Node, findall_by_attr, RenderTree

def debug(log_message):
    import datetime;
    debug_enabled = False
    # debug_enabled = True
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def print_tree(fs_tree):
    for pre, fill, node in RenderTree(fs_tree['root']):
        if node.type == 'dir':
            debug(f"{pre}{node.name} - ({node.type})")
        else:
            debug(f"{pre}{node.name} - ({node.type}) size: ({node.size})")

def get_node_path(node):
    debug(f'get_node_path: {get_node_path}')
    path = f"{node.name}"
    while(node.parent is not None):
        node = node.parent
        path = f"{node.name}/{path}"
    return path

def get_directories_under_path(current_path):
    debug(f'get_directories_under_path: {current_path}')
    return [directory.name for directory in list(filter(lambda node: node.type == 'dir', [children for children in current_path.children]))]

def get_directiory_size(current_path):
    debug(f'get_directiory_size: {current_path}')
    files = list(findall_by_attr(current_path, name='type' , value='file'))
    sum = 0
    for file in files:
        sum = sum + int(file.size)
    return  sum

def process_cd(path, fs_tree, current_path, last_line_proccesed):
    debug(f'process_cd to "{path}" from {current_path}')
    if path == '/' :
        current_path = fs_tree['root']
    elif path == '..' :
        current_path = current_path.parent
    else:
        if path in get_directories_under_path(current_path):
            debug(f'process_cd setting dir: "{path}" under: "{current_path}"')
            current_path = list(filter(lambda node: node.name == path and node.type == 'dir', [children for children in current_path.children]))[0]
        else:
            node = Node(path, parent = fs_tree[current_path], type='dir')
            node_path = get_node_path(node)
            fs_tree[node_path] = node
            current_path = fs_tree[node_path]

    last_line_proccesed = last_line_proccesed + 1
    return fs_tree, current_path, last_line_proccesed

def process_ls(console_output, fs_tree, current_path,last_line_proccesed):
    debug(f'process_ls: {console_output[last_line_proccesed]} in path: {current_path}')
    last_line_proccesed = last_line_proccesed + 1
    while (last_line_proccesed < len(console_output)):
        if console_output[last_line_proccesed][0] == '$':
            break

        debug(f'process_ls - processing line: {console_output[last_line_proccesed]}')
        if console_output[last_line_proccesed][0] == 'dir' :
            dirname = console_output[last_line_proccesed][1]
            if dirname not in get_directories_under_path(current_path):
                node = Node(dirname, parent = current_path, type='dir')
                node_path = get_node_path(node)
                fs_tree[node_path] = node
        else :
            filename = console_output[last_line_proccesed][1]
            node = Node(filename, parent = current_path, type='file', size=console_output[last_line_proccesed][0])
            node_path = get_node_path(node)
            fs_tree[node_path] = node

        print_tree(fs_tree)
        last_line_proccesed = last_line_proccesed + 1
    debug(f'process_ls Done current path state: {current_path}')
    return fs_tree, last_line_proccesed

def process_command(console_output, last_line_proccesed, file_system_tree, current_path):
    # TODO
    debug(f'process_command: {console_output[last_line_proccesed]}')
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
    root = Node('root', type='dir')
    file_system_tree['root'] = root
    current_path = file_system_tree[root.name]
    last_line_proccesed = 0

    while last_line_proccesed < len(console_output):
        debug(f'Processing: {console_output[last_line_proccesed]}')
        last_line_proccesed, file_system_tree, current_path = process_command(
            console_output,
            last_line_proccesed,
            file_system_tree,
            current_path)
    debug(f'file_system_tree: {file_system_tree}')
    return file_system_tree

def get_fs_tree_from_file(file_name):
    console_output_arr=[]
    input_file = open(file_name, 'r')
    for line in input_file:
        console_output_arr.append(line.strip().split(' '))
    input_file.close()

    return get_file_system(console_output_arr)

def get_total(file_name):
    total = 0

    file_system_tree = get_fs_tree_from_file(file_name)
    directories = findall_by_attr(file_system_tree['root'], name='type' , value='dir')
    debug(f"list all nodes: {[node for node in file_system_tree]}")
    debug(f"list directories: {directories}")
    total_disk=70000000
    used_disk=get_directiory_size(file_system_tree['root'])
    expected_free_space=30000000
    dirs_to_get_free_space=[]
    for directory in directories:
        debug(f'directory: {directory.name} size: {get_directiory_size(directory)}')
        directiory_size = get_directiory_size(directory)
        debug(f'used_disk - directiory_size: {used_disk - directiory_size} |  total_disk - expected_free_space: {total_disk - expected_free_space} ')
        if (used_disk - directiory_size) <= (total_disk - expected_free_space):
           dirs_to_get_free_space.append(directiory_size)
    debug(f'dirs_to_get_free_space: {dirs_to_get_free_space}')
    dirs_to_get_free_space.sort(reverse=True)
    debug(f'dirs_to_get_free_space: {dirs_to_get_free_space}')
    return dirs_to_get_free_space.pop()

## TESTS
debug('****************** TEST Input *************\n\n')
test_result = get_total("input_test")
expected_result = 24933642
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")
debug('TEST input Passed.')

debug('\n\n****************** Execution *************\n\n')
print(f"Result: {get_total('input')}")
