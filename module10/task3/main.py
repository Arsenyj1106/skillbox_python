import os
os.chdir('C:\Users\pirog\OneDrive\Рабочий стол\module10\task3')

def validate_registration(line):
    try:
        name, email, age = line.split()
        if not name.isalpha():
            raise NameError("Поле «Имя» содержит НЕ только буквы")
        if '@' not in email or '.' not in email:
            raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")
        age = int(age)
        if age < 10 or age > 99:
            raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")
    except IndexError:
        raise IndexError("НЕ присутствуют все три поля")
    except (NameError, SyntaxError, ValueError) as e:
        raise e

with open('registrations.txt', 'r') as infile, open('registrations_good.log', 'w') as good_file, open('registrations_bad.log', 'w') as bad_file:
    for line in infile:
        line = line.strip()
        try:
            validate_registration(line)
            good_file.write(line + '\n')
        except (IndexError, NameError, SyntaxError, ValueError) as e:
            bad_file.write(line + ' ' + str(e) + '\n')
