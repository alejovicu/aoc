def getMaxCalories(file_name):
    max_value = 0
    current = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            print(line.strip())
            if(line == "\n"):
                if current > max_value:
                    max_value = current
                    print(f"max: {max_value}")
                current = 0
            else:
                current = current + int(line)
                print(f"current: {current}")
                print(f"max: {max_value}")
    return max_value

print(getMaxCalories("test_input"))
print(getMaxCalories("input"))