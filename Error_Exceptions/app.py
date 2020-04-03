import sys

def ex_1():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    else:
        print('Error!')

def ex_2():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                             # but may be overridden in exception subclasses
        x, y = inst.args     # unpack args
        print('x =', x)
        print('y =', y)



if __name__ == "__main__":
    #The raise statement allows the programmer to force a specified exception to occur. 
    raise NameError('HiThere')       