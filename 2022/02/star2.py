def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def calc_points(oponent, you):
    debug(f"oponent: {oponent} | you: {you}")
    points = {
      'oponent': {
        'A': {'name':'rock','points':1},
        'B': {'name':'paper','points':2},
        'C': {'name':'scissors','points':3}
      },
      'you': {
        'X': {'name':'rock','points':1},
        'Y': {'name':'paper','points':2},
        'Z': {'name':'scissors','points':3}
      }
    }

    if oponent == "A":
      if you == "X":
        return 0 + points['you']['Z']['points']
      elif you == "Y":
        return 3 + points['you']['X']['points']
      else :
        return 6 + points['you']['Y']['points']
    
    if oponent == "B":
      if you == "X":
        return 0 + points['you']['X']['points']
      elif you == "Y":
        return 3 + points['you']['Y']['points']
      else :
        return 6 + points['you']['Z']['points']

    if oponent == "C":
      if you == "X":
        return 0 + points['you']['Y']['points']
      elif you == "Y":
        return 3 + points['you']['Z']['points']
      else :
        return 6 + points['you']['X']['points']

def getScore(file_name):
    score = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            debug(line.strip())
            moves = line.strip().split()
            score = score + calc_points(moves[0],moves[1])

    return score



test1_result = calc_points('A','Y')
test1_expected_result = 4
if test1_result != test1_expected_result:
    raise Exception(f"TEST_1 FAILED: Expected value: {test1_result}, got: {test1_expected_result}")

test2_result = calc_points('B','X')
test2_expected_result = 1
if test2_result != test2_expected_result:
    raise Exception(f"TEST_2 FAILED: Expected value: {test2_result}, got: {test2_expected_result}")

test3_result = calc_points('C','Z')
test3_expected_result = 7
if test3_result != test3_expected_result:
    raise Exception(f"TEST_3 FAILED: Expected value: {test3_result}, got: {test3_expected_result}")


test_result = getScore("input_test")
expected_result = 12
if test_result != expected_result:
    raise Exception(f"TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {getScore('input')}")