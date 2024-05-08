#*args and *kwargs are special python keywords that are used to pass the variable length of arguments to a function
##   *args
# allows us to pass a variable number of non-keyword arguments to a function.
def multiply(*args):
    product=1

    for i in args:
        product = product * i

    print(args)
    return product
print(multiply(1,2,3,4,5))
