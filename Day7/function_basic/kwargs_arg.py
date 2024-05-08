# **kwargs
#**kwargs allows us to pass any number of keyword argument.
#keyword arguments mean that they contain a key-value pair, like a python dictionary.

def display(**kwargs):

    for(key,value) in kwargs.items():
        print(key,'->',value)
display(india='delhi',srilanka='colombo',mepal='kathmandu')