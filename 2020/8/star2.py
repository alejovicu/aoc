inputFile = open('input', 'r')
lines = [line.strip() for line in inputFile.readlines()]
inputFile.close()

already_done = {
}

result = {
    "stack_idx": 0,
    "value": 0
}

def exec(result, operation):
    ops = operation.split(" ")
    print(ops)
    if ops[0] == "nop" :
        result["stack_idx"] = result["stack_idx"] + 1
    elif ops[0] == "acc" :
        result["stack_idx"] = result["stack_idx"] + 1
        result["value"]     = result["value"] + int(ops[1])
    else:
        result["stack_idx"] = result["stack_idx"] + int(ops[1])

def exec_operation(result, operation_list):
    while result["stack_idx"] != len(operation_list):
        if result["stack_idx"] in already_done:
            return result
        else :
            already_done[result["stack_idx"]] = 1
            exec(result, operation_list[result["stack_idx"]])

exec_operation(result, lines)
print(result)
