# Open a file
fo = open("input", "r")
content = fo.read().split("\n")
fo.close()
valid=0
for line in content :
  line_arr      = line.split(" ")
  pos1          = int(line_arr[0].split("-")[0]) - 1
  pos2          = int(line_arr[0].split("-")[1]) - 1
  string_search = line_arr[1].split(":")[0]
  password      = line_arr[2]
  if password[pos1] == string_search and password[pos2] != string_search :
      valid = valid + 1
  if password[pos1] != string_search and password[pos2] == string_search :
      valid = valid + 1
print(valid)