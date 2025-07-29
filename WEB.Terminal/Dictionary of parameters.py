import sys


def main():
    args = sys.argv[1:]
    sort_flag = False
    if "--sort" in args:
        sort_flag = True
        args.remove("--sort")
    key_value_pairs = []

    for arg in args:
        if "=" in arg:
            key, value = arg.split("=", 1)
            key_value_pairs.append((key, value))
    if sort_flag:
        key_value_pairs.sort(key=lambda x: x[0])

    for key, value in key_value_pairs:
        print(f"Key: {key} Value: {value}")


if __name__ == "__main__":
    main()
