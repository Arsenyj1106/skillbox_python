with open('numbers.txt', 'r') as file:
  numbers = file.read().split()

sum_of_numbers = sum(int(num) for num in numbers)

with open('answer.txt', 'w') as file:
  file.write(str(sum_of_numbers))