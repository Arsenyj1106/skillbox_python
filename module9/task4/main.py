import os
os.chdir("C:\Users\pirog\OneDrive\Рабочий стол\module9\task4")

with open("first_tour.txt", "r") as input_file:
    k = int(input_file.readline().strip())
    data = input_file.readlines()

filtered_data = []
for line in data:
    parts = line.split()
    if len(parts) == 3:
        last_name, first_name, points = parts
        points = int(points)
        if points > k:
            filtered_data.append((last_name, first_name[0], points))

filtered_data.sort(key=lambda x: x[2], reverse=True)

with open("second_tour.txt", "w") as output_file:
    output_file.write(str(len(filtered_data)) + "\n")
    for i, (last_name, first_initial, points) in enumerate(filtered_data, start=1):
        output_file.write(f"{i}) {first_initial}. {last_name} {points}\n")