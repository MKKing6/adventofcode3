import re
input = open("input.txt").readlines()
sum = 0

for c, line in enumerate(input):
  digits = re.findall(r'\d+', line)
  if digits:
    for i in digits:
      for lineCheck in range(c - 1, c + 2):
        if lineCheck >= 0 or lineCheck < len(input):
          for charCheck in range(line.index(i) - 1, line.index(i) + len(i) + 1):
            if charCheck >= 0 or charCheck < len(line):
              if not line[charCheck].isdigit() and line[charCheck] != ".":
                print(line[charCheck])
                

