mydict = {}

def myfunction():
    temp = 0

mylist = ['a', 'b', 'c']

data = {'b': mydict, 'c': myfunction}

for key in mylist[1:]:
    element = data.get(key)
    if isinstance(element, dict):
        print("is dict")
    elif callable(element):
        print("is func")
