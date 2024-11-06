# Ввод трех целых чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Условная конструкция для определения количества одинаковых чисел
if first == second == third:  # Если все три числа равны
    print(3)
elif first == second or first == third or second == third:  # Если хотя бы два числа равны
    print(2)
else:  # Если все числа разные
    print(0)