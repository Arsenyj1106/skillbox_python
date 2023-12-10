import os

def get_directory_info(path):
    total_size = 0
    total_files = 0
    total_subdirectories = 0

    for root, directories, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
            total_files += 1
        total_subdirectories += len(directories)

    return total_size, total_files, total_subdirectories

path = input("Введите путь к каталогу: ")

size, files, subdirectories = get_directory_info(path)
size_in_kb = size / 1024
print(f"Размер каталога (в Кбайтах): {size_in_kb}")
print(f"Количество подкаталогов: {subdirectories}")
print(f"Количество файлов: {files}")