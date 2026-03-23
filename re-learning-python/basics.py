import sys
# use python basics.py in cmd to run
# this file is for learning basic syntax and features of python as reminder for myself, basically just notes while following w3schools python tutorial
print("Hello, World!") 
print(sys.version)

if 5 > 2:
    print("Five is greater than two") # note indetation is very important it indicates the block of code 
     # print("5 is greater than 2") this line gives error because of the indentation in the same block of code is the same
if 5 > 2:
 print("five is greater than two")

x = 5 # dont need to declare the type of variable in python like in other programming languages.
y = "text"

print(x, y)
print(type(x), type(y)) #with type we can check the type of variable

# also in python you dont need to end line with semicolon like in other programming languages statement ends when the line ends.
# but if you are typing multiple statemets in same line then you can use semicolon to separate them like print(x); print(y)

print("hey lets print words on same line...", end=" ")
print("These words are on the same line.")

print(1234) # when printing numbers you dont put nubers inside quotes
print(5 + 3) # math also works in print statement
print("5 * 2 = ", x * 2)

"""
multi
line
comment
"""
x = 4
x = "Sally"
print(x) # Sally is printed because value of x is reassigned to "Sally" so all previously declared values of x are overwritten by the latest

x = str(3) # data types can be specified if wanted but its not necessary now x is a string '3', y is integer 3 and z is float 3.0
y = int(3)
z = float(3)
print(type(x), type(y), type(z))

#note when declaring variables you can only use letters, numbers and underscores and variable can't start with a number
# and obviously they are case sensitive and no whitespaces and dashes in variable names

x, y, z = "Apple", "Strawberry", "Lingonberry" # multiple variables can be declered in one line like this
print(x)
print(y)
print(z) #or print(x, y, z) to prin all in one line or print(x + y + z) to concatenate strings but if it is integers it will add them together

# if you want you can assign same value to multple variables like this: x = y = z = "Blueberry"

fruits = ["apple", "banana", "cherry"] #collection of values = list
x, y, z = fruits
print(x)
print(y)
print(z) # unpacking list into variables

# when variable is declared outside of function it is global variable and can be used by everyone.
x = "interesting"

def myfunc():
   print("PYthon is " + x)

myfunc()

# and when variable is declared inside a function it is local variable and can only be used inside that function.

def myfunc2():
   x = "awesome"
   print("PYthon is " + x)

myfunc2()

print("Python is " + x)
# note you can also make local variable global by defining it as global inside the function like this: global x  x= "something"
"""
python datatypes:
for text: str = string
for numbers: int = integer, float = floating number, complex = complex number
for sequence types: list, tuple, range -> collection of ordered values
for mapping: dict = dictionary -> collection of key-value pairs
for set types: set, frozenset -> unordered collection of unique items
for boolean: bool = boolean -> true or false
for binary types: bytes, bytearray, memoryview  -> for handling binary data
and none type: NoneType -> represents absence of value or null value
"""
x = "Hello World"
print(x, type(x))
x = 20
print(x, type(x))
x = 20.5
print(x, type(x))
x = 1j
print(x, type(x))
x = ["apple", "banana", "cherry"]
print(x, type(x))
x = ("apple", "banana", "cherry")
print(x, type(x))
x = range(6)
print(x, type(x))
x = {"name" : "John", "age" : 36}
print(x, type(x))
x = {"apple", "banana", "cherry"}
print(x, type(x))
x = frozenset({"apple", "banana", "cherry"})
print(x, type(x))
x = True
print(x, type(x))
x = b"Hello"
print(x, type(x))
x = bytearray(5)
print(x, type(x))
x = memoryview(bytes(5))
print(x, type(x))
x = None
print(x, type(x))

# you can convert datatypes for example numbers like this:
x = 1
y = 4.5
z = 2j  # complex cannot be converted to other number types but others can be made to complex

a = float(x)
b = int(y)
c = complex(x)

print(a, type(a))
print(b, type(b))
print(c, type(c))

# python does not have random() function like other programming languages do so you need to import random module to use random functions.
import random # typically module imports are done at the beginning of the code.

print(random.randrange(1, 10)) # random number between 1 and 9

# earlier i noted the multiline comment, it can also be used as multiline string when assigned to a variable
a = """multiline text going hard,
and keeps going on and on,
until it reaches the end of the quotes."""
print(a) # linebreaks are inserted in same position as in the code

#like in other languages have char datatype but in python there is only string type that are arrays of characters so if you want to get single character do it liek this:
a = "Hello"
print(a[1]) # this should print the letter "e" because string starts with index 0 which in this case is letter H -> 1 is "e"
# and bevause strings are arrays we can loop through the characters in a string with for loop:
for x in "apple":
   print(x) # this loop will print each character in string apple in a new line

#then we also can get the length of a string using len() function:
a = "Hello, World!"
print(len(a)) # this prints the number of characters in a string a

# we can also check if a certain phrase or character is present in a string using keyword in:
txt = "the best things in life are free!"
print("free" in txt) # in returns boolean value

if "free" in txt:
   print("yes, 'free' is present.") # but we can make conditional statemnt with if statement to print if the condition is true, in this case free is True in txt

# there is also NOT IN keyword to check if phrace or character is not present in string:
print("expensive" not in txt) # and this shoudl return True because expensive is not in txt
#and same in if statement:
if "expensive" not in txt:
   print("no, 'expensive' is NOT present.")

# if we want to slice characters from string we can specify start and end index:
b = "I am hungry"
print(b[2:5]) # this should print "am " because string starts from 0 that is I -> space is 1 and so on until we start our index 2 that is "a" and end to index 5 whick is the spce after am

# start from the beginning of the string:
print(b[:5]) # prints "I am "
# start from 2 to end:
print(b[2:])

# then we can also use negative to start from the end of the string:
print(b[-5:-2]) # prints "ung"
print(b[-7:])

#modifying strings:
a = " I am hungry "
print(a.upper()) #prints uppercase version of string
print(a.lower()) #prints lowercase
print(a.strip()) #removes whitespace from beginning and end of string
print(a.replace("u", "a")) #replaces all "u" characters with "a"
print(a.split(",")) # splits strings into substrings and the text between separators becomes a list where each word becomes a list item

#earlier i noted that we cant combine strings and numbers but it can be done by using format strings:
age = 66
txt = f"Erkki is getting closer to retirement, he is {age} years old."
print(txt) #in f strings simply put f in front of the string literal and curly brackets {} as placeholder for the variables and other operations

#you can also add modifiers to f strings
price = 74
txt = f"The price for food after delivery fee is {price:.2f} euros." # added .2f to format 2 decimal palces
print(txt)

txt = f"The price for food after delivery fee is {18 * 3} euros."
print(txt)

# Escape characters are used to insert characters that are illegal in a string:
txt = "We are the so-called \"Vikings\" from the north." # double quotes are illegal in string but using backslash we can insert them in string
print(txt)

"""
Escape characters:
\' -> single quote
\\ -> backslash
\n -> new line
\r -> carriage return
\t -> tab
\b -> backspace
\f -> form feed
\ooo -> octal value
\xhh -> hexadecimal value
"""

""" more in w3schools
string methods:
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""



