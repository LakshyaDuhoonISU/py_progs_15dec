#file my_module is imported and sum of two numbers is done using the function from my_module module
from importlib import reload #reload module is imported from the importlib module
#from my_module import Addition,Subtraction #used to import only a particular class or method from a module
import my_module as mm #my_module is given an alias name as mm  
reload(mm) #reload the module, used where we work on multiple cells like google collab, jupyter notebook
#a=mm.Addition()
b=float(input("Enter a number: "))
c=float(input("Enter another number: "))
#a.add(b,c)
d=mm.Subtraction() 
d.sub(b,c)

