print("hello world")

#indentation matters for python.
#python uses indentation to indicate a block of code
#has to be at least 1 space of indentation
if 5 > 2:
    print("Five is greater than 2")

#VARIABLES-------------------

#python has no command for declaring variables
#variable is created the moment you assign a value to it

x = 5
y = "john"
print(x)
print(y)

#variables do not need to be delcared with any particular type
#it can change type after theyv'e been set

x = 4   #x is of type int
x = "Sally" #x is now of type str
print(x)

#casting variables
x = str(3)
y = int(3)
z = float(3)

#getting the type using type()

x = 5
y = "john"
print(type(x))
print(type(y))

#strings can be delcared using single or double quotes
x = "double quotes"
x = 'single quotes'
print(x)

#NAMING VARIABLES ----------------------
    #a variable name must start with a letter or underscore
    #a variable name cannot start with a number
    #a variable name can only contain alpha-numeric characters and underscores
    #variable names are case-sensitvie

myvar = "John"
my_var = "John"
_my_var = "john"
myVar = "john"
MYVAR = "john"
myvar2 = "john"

#multi word variables can use Camel Case, Pascal Case, or Snake case
myVariableName = "john" #Camel
MyVariableName = "john" #Pascal
my_variable_name = "john" #Snake

#you can assign multiple variables and values in one line
x, y, z = "Orange", "Banana", "cherry"
x = y = z = "Orange"

#you can use collections of values in a list / tuple
#this can be "unpacked" by python
fruits = [ "Orange", "Banana", "cherry"]
x, u, z = fruits
print(x)
print(y)
print(z)


#GLOBAL VARIABLES ------------------

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#you can create global variables inside of a function

def myfunc():
    global x #use the global keyword
    x = "fantastic"

myfunc()
print("Python is " + x)


#BUILT-IN DATA TYPES ----------------------
#text type: str
#numeric types: int, float, complex
#sequence types: list, tuple, range
#mapping type: dict
#set type: set, frozenset
#boolean type: bool
#binary types: bytes, bytearray, memoryview
#nonetype: NoneType

x = "Hello World"                   #STR
x = 20                              #int
x = 20.5                            #float
x = 1j                              #complex
x = ["Apple", "Banana"]             #list
x = ("apple", "banana")             #tuple
x = range(6)                        #range
x = {"Name" : "John", "age" : 36}   #dict
x = {"apple", "banana", "cherry"}   #set
x = True                            #bool
x = None                            #nonetype


#STRINGS ---------------------
a = "hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are arrays of characters
a = "hello"
print(a[1])
