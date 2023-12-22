#a file is created with a class Addition that has a method to add two numbers
class Subtraction:
    def sub(self,x,y):
        print("Difference:",x-y)
class Division:
    def div(self,x,y):
        print("Division:",x/y)
if __name__=="__main__": #if block is executed as we are in main module file
    print("Executed directly")
    class Addition:
        def add(self,x,y):
            print("Sum:",x+y)
else: #else block is executed when we import the module
    print("Executed after import")