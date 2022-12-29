def debug(log_message):
    import datetime;
    debug_enabled = False
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def get_visible_trees_count(grid):
  rows = len(grid)
  cols = len(grid[0])

  # Check trees in the first and last rows
  count = rows*2 + (cols-2)*2
  debug(f"rows: {rows}")
  debug(f"cols: {cols}")
  debug(f"outside count: {count}")


  # Check trees in the interior of the grid
  for row in range(1, rows-1):
    for col in range(1, cols-1):
      tree = grid[row][col]
      debug(f"tree: {tree}")
      # Check if tree is visible from left
      visible_from_left = True
      for i in range(col-1, -1, -1):
        debug(f"tree: {tree} vs left {grid[row][i]}")
        if grid[row][i] >= tree:
          visible_from_left = False
          break
      if visible_from_left:
        debug(f"tree: {tree} is visible from left")
        count += 1
        continue

      # Check if tree is visible from right
      visible_from_right = True
      for i in range(col+1, cols):
        if grid[row][i] >= tree:
          visible_from_right = False
          break
      if visible_from_right:
        debug(f"tree: {tree} is visible from right")
        count += 1
        continue

      # Check if tree is visible from top
      visible_from_top = True
      for i in range(row-1, -1, -1):
        if grid[i][col] >= tree:
          visible_from_top = False
          break
      if visible_from_top:
        debug(f"tree: {tree} is visible from top")
        count += 1
        continue

      # Check if tree is visible from bottom
      visible_from_bottom = True
      for i in range(row+1, rows):
        if grid[i][col] >= tree:
          visible_from_bottom = False
          break
      if visible_from_bottom:
        debug(f"tree: {tree} is visible from bottom")
        count += 1
        continue

  return count

def get_grid_from_file(file_name):
    grid = []
    input_file = open(file_name, 'r')
    for line in input_file:
        grid.append([int(x) for x in list(line.strip())])
    input_file.close()
    return grid

def get_total(file_name):
    grid = get_grid_from_file(file_name)
    return get_visible_trees_count(grid)

### TESTS

test_result = get_grid_from_file('input_test')
test_expected_result = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]]
if test_result != test_expected_result:
    raise Exception(f"TEST 1 FAILED: Expected value: {test_expected_result}, got: {test_result}")


test_result = get_total("input_test")
expected_result = 21
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_total('input')}")

