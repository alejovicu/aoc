def debug(log_message):
    import datetime;
    debug_enabled = True
    if debug_enabled:
        print(f"[{datetime.datetime.now()}] - [DEBUG] - {log_message}")

def get_trees_scenic_score(grid):
  rows = len(grid)
  cols = len(grid[0])

  max_scenic_score = 0

  for row in range(1, rows-1):
    for col in range(1, cols-1):
      tree = grid[row][col]

      view_count_top = 0
      for i in range(row-1, -1, -1):
        if grid[i][col] < tree:
          view_count_top = view_count_top +1
        else:
          view_count_top = view_count_top + 1
          break
      debug(f"tree: {tree} view_count_top {view_count_top}")

      view_count_left = 0
      for i in range(col-1, -1, -1):
        debug(f"left - tree: {tree} vs {grid[row][i]}")
        if grid[row][i] < tree:
          view_count_left = view_count_left + 1
        else:
          view_count_left = view_count_left + 1
          break
      debug(f"tree: {tree} view_count_left {view_count_left}")

      view_count_right = 0
      for i in range(col+1, cols):
        if grid[row][i] < tree:
          view_count_right = view_count_right + 1
        else:
          view_count_right = view_count_right + 1
          break
      debug(f"tree: {tree} view_count_right {view_count_right}")

      view_count_bottom = 0
      for i in range(row+1, rows):
        if grid[i][col] < tree:
          view_count_bottom = view_count_bottom +1 
        else:
          view_count_bottom = view_count_bottom + 1
          break
      debug(f"tree: {tree} view_count_top {view_count_top}")

      curent_tree_scenic_score = view_count_left * view_count_right * view_count_top * view_count_bottom
      debug(f"tree: {tree} | ({view_count_top} * {view_count_left} * {view_count_right} * {view_count_bottom})")
      debug(f"tree: {tree} | tree_scenic_score: {curent_tree_scenic_score}")
      if curent_tree_scenic_score > max_scenic_score:
          max_scenic_score = curent_tree_scenic_score
  return max_scenic_score

def get_grid_from_file(file_name):
    grid = []
    input_file = open(file_name, 'r')
    for line in input_file:
        grid.append([int(x) for x in list(line.strip())])
    input_file.close()
    return grid

def get_total(file_name):
    grid = get_grid_from_file(file_name)
    return get_trees_scenic_score(grid)

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
expected_result = 8
if test_result != expected_result:
    raise Exception(f"INPUT TEST FAILED: Expected value: {expected_result}, got: {test_result}")

print(f"Result: {get_total('input')}")

