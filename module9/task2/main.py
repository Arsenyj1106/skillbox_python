with open('zen.txt', 'r') as file:
  lines = file.readlines()
  for line in reversed(lines):
      print(line.strip())