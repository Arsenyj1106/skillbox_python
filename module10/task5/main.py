import math

def safe_square_root(number):
    try:
        if number < 0:
            raise ValueError("Отрицательные числа не имеют действительных квадратных корней.")
        result = math.sqrt(number)
        return f"Квадратный корень числа {number} равен {result}"
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

try:
    number = float(input("Введите число для вычисления квадратного корня: "))
    result = safe_square_root(number)
    print(result)
except ValueError as e:
    print(f"Ошибка: {str(e)}")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")