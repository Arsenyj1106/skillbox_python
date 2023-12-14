import os
os.chdir('C:\Users\pirog\OneDrive\Рабочий стол\module15')


class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            self.file = open(self.filename, 'w')
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with File("test.txt", "r") as file:
    if file:
        for line in file:
            print(line.strip())


