import argparse


def main():
    parser = argparse.ArgumentParser(description="Калькулятор 3.0")
    parser.add_argument('numbers', nargs='*', help="Целочисленные параметры")  # Принимаем аргументы как строки

    try:
        args = parser.parse_args()
        numbers = args.numbers

        if len(numbers) == 0:
            print("NO PARAMS")
        elif len(numbers) == 1:
            print("TOO FEW PARAMS")
        elif len(numbers) == 2:
            try:
                num1 = int(numbers[0])
                num2 = int(numbers[1])
                print(num1 + num2)
            except ValueError:
            
                print("ValueError")
        else:
            print("TOO MANY PARAMS")
    except Exception as e:
        print(type(e).__name__)


if __name__ == "__main__":
    main()