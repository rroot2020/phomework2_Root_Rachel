def sum(x, y):

    return x + y

def mul(x, y): 
    z = x * y
    return z
def print_pretty(a):
    print("The result is {:.3f}.".format(a))

    print_pretty(mul(10, sum(3, 5)))

    