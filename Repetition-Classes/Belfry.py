class LittleBell:
    def sound(self):
        print("ding")


class BigBell:
    def __init__(self):
        self.next_ding = True

    def sound(self):
        if self.next_ding:
            print("ding")
        else:
            print("dong")
        self.next_ding = not self.next_ding


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print("...")