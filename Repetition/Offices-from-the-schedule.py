from collections import defaultdict


rooms = defaultdict(list)
while True:
    try:
        s = input().strip()
        if not s:
            continue
        if s.isalpha():  
            continue
        *sub, room = s.rsplit(' ', 1)
        sub = ' '.join(sub)
        room = int(room)
        if sub not in rooms[room]:
            rooms[room].append(sub)
    except EOFError:
        break

for room in sorted(rooms):
    print(f"{room}: {', '.join(rooms[room])}")
