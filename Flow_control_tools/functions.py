# **name = it receives a dictionary
# *name = receives a tuple 
def foo(string, *args, **keyword): 
    print(string)

    if args:
        print(args)

    if keyword:
        print(keyword)
        if 'name' in keyword:
            print(keyword['name'])

def concatenate(*args, sep='/'):
    return sep.join(args)

if __name__ == "__main__":
    tupla = (1,2,3,4,5)
    dictionary = {"name" : "simone", "surename" : "vaiasinni"}
    
    #foo("Hello world", 1,2,3,4,5, name="simone", surename="vaiasinni" )
    #foo("Hello world", 1,2,3,4,5, **dictionary)

    print(concatenate("home", "simone", "desktop"))


