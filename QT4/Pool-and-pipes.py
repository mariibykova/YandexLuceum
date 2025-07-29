def main():
    with open("pipes.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()
    try:
        empty_index = lines.index("")
    except ValueError:
        print("Неверный формат файла pipes.txt: отсутствует пустая строка.")
        return
    pipe_times = lines[:empty_index]
    pipe_times = [float(t.strip()) for t in pipe_times if t.strip()]
    used_pipe_lines = lines[empty_index + 1:]
    used_pipes_list = []
    for line in used_pipe_lines:
        used_pipes_list.extend(line.split())
    used_pipes_indexes = [int(pipe_number) - 1 for pipe_number in used_pipes_list]
    total_rate = 0.0
    for idx in used_pipes_indexes:
        total_rate += 1.0 / pipe_times[idx]
    if total_rate == 0:
        result_minutes = 0
    else:
        total_time_hours = 1.0 / total_rate
        result_minutes = total_time_hours * 60
    with open("time.txt", "w", encoding="utf-8") as out:
        out.write(str(result_minutes))


if __name__ == "__main__":
    main()
