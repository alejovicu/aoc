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
        return 3 + points['you']['X']['points']
      elif you == "Y":
        return 6 + points['you']['Y']['points']
      else :
        return 0 + points['you']['Z']['points']
    
    if oponent == "B":
      if you == "X":
        return 0 + points['you']['X']['points']
      elif you == "Y":
        return 3 + points['you']['Y']['points']
      else :
        return 6 + points['you']['Z']['points']

    if oponent == "C":
      if you == "X":
        return 6 + points['you']['X']['points']
      elif you == "Y":
        return 0 + points['you']['Y']['points']
      else :
        return 3 + points['you']['Z']['points']

def getScore(file_name):
    score = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            debug(line.strip())
            moves = line.strip().split()
            score = score + calc_points(moves[0],moves[1])

    return score

test_result = getScore("input_test")
expected_result = 15
if test_result != expected_result:
    raise Exception(f"TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {getScore('input')}")