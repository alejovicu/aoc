def getMaxCalories(file_name):
    top_3 = [0,0,0]
    current = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            print(line.strip())
            if(line == "\n"):
                if current > top_3[0]:
                    top_3[2] = top_3[1]
                    top_3[1] = top_3[0]
                    top_3[0] = current
                    print(f"top_3[0]: {top_3[0]}")

                elif current > top_3[1]:
                    top_3[2] = top_3[1]
                    top_3[1] = current
                    print(f"top_3[1]: {top_3[1]}")
                elif current > top_3[2]:
                    top_3[2] = current
                    print(f"top_3[2]: {top_3[2]}")
                current = 0
            else:
                current = current + int(line)
                print(f"current: {current}")
                print(f"max: {top_3}")
    return sum(top_3)

print(getMaxCalories("test_input"))
print(getMaxCalories("input"))