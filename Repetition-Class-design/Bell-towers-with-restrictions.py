class Bell():
    def __init__(self, *args, **kwargs):
        self.args = []
        self.kwargs = kwargs
        for i in args:
            self.args.append(i)
 
    def print_info(self):
        if self.args or self.kwargs:
            a = []
            keys = sorted(self.kwargs.keys())
            for i in keys:
                a += [i + ': ' + self.kwargs[i]]
            kkk = ', '.join(a)
            a = []
            for i in self.args:
                a.append(i)
            yyy = ', '.join(a)
            if yyy and not kkk:
                print(yyy)
            elif kkk and not yyy:
                print(kkk)
            elif kkk and yyy:
                print('; '.join([kkk, yyy]))
        else:
            print('-')
 
 
class BigBell(Bell):
    a = 0
 
    def sound(self):
        if not self.a:
            print('ding')
            self.a = 1
        else:
            print('dong')
            self.a = 0
 
    def info(self):
        return BigBell
 
    def info0(self):
        return 'BigBell'
 
 
class LittleBell(Bell):
    def sound(self):
        print("ding")
 
    def info(self):
        return LittleBell
 
    def info0(self):
        return 'LittleBell'
 
 
class BellTower:
    def __init__(self, *args):
        self.bells = []
        for arg in args:
            self.bells.append(arg)
 
    def append(self, bell):
        self.bells.append(bell)
 
    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')
 
    def print_info(self):
        n = 0
        for i in self.bells:
            n += 1
            print(f'{n} {i.info0()}')
            i.print_info()
        print('')
 
 
class SizedBellTower(BellTower):
    def __init__(self, *args, size=10):
        self.size = size
        self.bells = []
        n = 0
        for arg in args:
            n += 1
            if n > self.size:
                self.bells.append(arg)
                del self.bells[0]
            else:
                self.bells.append(arg)
 
    def append(self, bell):
        if len(self.bells) == self.size:
            self.bells.append(bell)
            del self.bells[0]
        else:
            self.bells.append(bell)
 
 
class TypedBellTower(BellTower):
    def __init__(self, *args, bell_type=LittleBell):
        self.bell_type = bell_type
        self.bells = []
        for arg in args:
            if arg.info() == self.bell_type:
                self.bells.append(arg)
 
    def append(self, bell):
        if bell.info() == self.bell_type:
            self.bells.append(bell)