def add(x,y):
    print(x+y)
if __name__=="__main__":
    print(__name__) #as the control is in the module file, __name__ will return as main
    add(3,7)
else:
    print("Module name of first after import:",__name__) #__name__ will return the name of the module
    print("First is imported")