import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Чтение файла с дополнительными опциями.")
    parser.add_argument("filename", help="Имя файла для чтения")
    parser.add_argument("--count", action="store_true", help="Вывести количество строк")
    parser.add_argument("--num", action="store_true", help="Вывести номера строк")
    parser.add_argument("--sort", action="store_true", help="Сортировать строки")

    args = parser.parse_args()

    try:
        with open(args.filename, 'r') as file:
            lines = file.readlines()

            if args.sort:
                lines.sort()

            for i, line in enumerate(lines):
                if args.num:
                    print(f"{i} {line.strip()}")
                else:
                    print(line.strip())

            if args.count:
                print(f"rows count: {len(lines)}")

    except FileNotFoundError:
        print("ERROR")


if __name__ == "__main__":
    main()