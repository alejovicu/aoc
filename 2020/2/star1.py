# Open a file
fo = open("input", "r")
content = fo.read().split("\n")
fo.close()
valid=0
for line in content :
  line_arr      = line.split(" ")
  pol_min       = int(line_arr[0].split("-")[0])
  pol_max       = int(line_arr[0].split("-")[1])
  string_search = line_arr[1].split(":")[0]
  if line_arr[2].count(string_search) >= pol_min and line_arr[2].count(string_search) <= pol_max :
      valid = valid + 1
print(valid)