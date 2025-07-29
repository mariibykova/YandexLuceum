import random
 
def random_line(afile):
    try:
        line = next(afile)
        for num, aline in enumerate(afile, 2):
            if random.randrange(num):
                continue
            line = aline
        print(line)
    except StopIteration:
        return
 
 
random_line(open("lines.txt"))