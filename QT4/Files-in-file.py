def convert_to_bytes(size_str, unit):
    size = float(size_str)
    units = ["B", "KB", "MB", "GB", "TB"]
    power = units.index(unit)
    return int(size * (1024**power))


def convert_from_bytes(size_in_bytes):
    units = ["B", "KB", "MB", "GB", "TB"]
    power = 0
    while size_in_bytes >= 1024 and power < len(units) - 1:
        size_in_bytes /= 1024
        power += 1
    size_in_unit = round(size_in_bytes)
    return size_in_unit, units[power]


def main():
    files_by_ext = {}
    with open("input.txt", "r", encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            file_name = parts[0]
            size_str = parts[1]
            unit = parts[2]
            if "." in file_name:
                ext = file_name.split(".")[-1]
            else:
                ext = ""
            size_in_bytes = convert_to_bytes(size_str, unit)
            if ext not in files_by_ext:
                files_by_ext[ext] = []
            files_by_ext[ext].append((file_name, size_in_bytes))

    with open("output.txt", "w", encoding="utf-8") as fout:
        for ext in sorted(files_by_ext.keys()):
            files_by_ext[ext].sort(key=lambda x: x[0])
            for file_info in files_by_ext[ext]:
                fout.write(file_info[0] + "\n")
            fout.write("----------\n")
            total_size_bytes = sum(x[1] for x in files_by_ext[ext])
            total_size, total_unit = convert_from_bytes(total_size_bytes)
            fout.write(f"Summary: {total_size} {total_unit}\n\n")


if __name__ == "__main__":
    main()
