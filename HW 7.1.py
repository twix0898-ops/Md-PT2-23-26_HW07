try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    operation = input("Выберите операцию(Введите +, -, * или /): ")

    if operation == "+":
        print(number1 + number2)
        result = number1 + number2
    elif operation == "-":
        print(number1 - number2)
        result = number1 - number2
    elif operation == "*":
        print(number1 * number2)
        result = number1 * number2
    elif operation == "/":
        print(number1 / number2)
        if number2 == 0:
            print("На ноль делить нельзя!")
            result = None
        else:
            result = number1 / number2
    elif operation == "**":
        print(number1 ** number2)
        result = number1 ** 2
    else:
        print("Ошибка операции")
        result = None
    print(result)

except ValueError:
    print("Ошибка: введите числа")