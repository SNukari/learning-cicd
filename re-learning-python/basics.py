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
print("data types: ")
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
print("datatype conversions: ")
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
print("random number: ")
print(random.randrange(1, 10)) # random number between 1 and 9
print("multilines and strings: ")
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
print("modifying strings: ")
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
\\ooo -> octal value
\\xhh -> hexadecimal value"""
# then we have string methods

"""
more in w3schools
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

#booleans are pretty much same as in other programming languages -> True and False depending on the condition of statement.
print("boolean values: ")
print(5 > 2) # <- true
print(5 < 2) # <- false

a = 5
b = 100

if b > a:
   print("b is greater than a")
else:
   print("b is not greater than a")

#we can also evaluate values and variables
print(bool("Hello")) # should return true because string is not empty
print(bool(5)) # should return true because number is not zero
print(bool("")) # empty string returns false
print(bool(0))  # zero returns false same goes with any empty variable like lists, tuples, sets, etc.

class classtwo():
   def __len__(self):
      return 0
   
myobject = classtwo()
print(bool(myobject)) # returns false because class __len__ method returns 0 therefore myobject is seen as empty value
 #functions can also return boolean values: return True this can be used in if statements
def myfunction():
   return True # we can just return true or false and if else statemnt will work based on that value
if myfunction():
   print("YES! it is true")
else:
   print("NO! it is false")

# then we also can check if object is certain datatype using isinstance() function:
x = 20
print(isinstance(x, int)) # we are checking if x is instance of int datatype. isinstance returns true or false 

#Operators are similiar to other programming languages:
# we have arithmetic operators: +, -, *, /, %, **(as exponential), //(as floor division)
print("arithmetic operators: ")
sum1 = 3 + 2
sum2 = sum1 + 20
print(sum2)
subtract1  = sum2 - 10
print(subtract1)
multiply1 = subtract1 * 2
print(multiply1)
divide1 = multiply1 / 2
print(divide1)
modulus1 = divide1 % 3
print(modulus1)
expotential1 = 2 ** 3
print(expotential1)
floordivision1 = 7 // 3
print(floordivision1) # rounds down the result to nearest whole number. division returns float but floordivision returns integer

#then there is assigment operators: =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=, :=
print("assigment operators: ")
x = 5
x += 3 #same as x = x + 3
print(x)
x -= 3 #same as x = x-3
print(x)
x *= 3 #same as x = x *3
print(x)
x /= 3 #same as x = x/3
print(x)
x %= 3 #same as x = x%3
print(x)
x **= 3 #same as x = x**3
print(x)
x //= 3 #same as x = x//3
print(x)

# walrus operator := is used to assign values to variables as part of a larger expression. from w3schools:
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

print("comparison operators: ")
#comparisons are ==, !=, >, <, >=, <=
x = 10
y = 7
print(x == y) #returns true or false
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#comparison operators can be chained:
x = 3
print(1 < x < 5) #returns true because it makes sense
print(1 > x < 5) #returns false

print("logical operators: ")
# and, or and not also
a = 5
print(a > 3 and a < 10) #should be true
print(a > 3 or a < 4)  #should be true only one of the conditions needs to be true
print(not(a > 3 and a < 10)) #should be false because normal codition is true but we negate it with not so it returns false

print("identity operators: ")
#identity opreators is and is not compare memory locations of two objects adn returns true if the are the same
#note value is not same as identity, two different objects can have same value but they are not the same object in memory
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x == y) #this is true because == compares values of x and y
print(x is y) #this is false because they are different objecrs in memory
print(x is not y) #true
z = y
print(z is y) #true because z and y are same object in memory

print("membership operators: ")
#in and not in are used to test if a sequence is present in object
x = ["apple", "banana", "cherry"]
print("banana" in x) #returns true because banana is in list x
print("grape" in x) #returns false
print("banana" not in x) # false because it is in x
print("grape" not in x) #true
#membership operators work also in strings and you can check if certain character or phrase is in or is not in string

print("bitwise operators: ")
# bitwise operators are used to compare binary numbers, they are &, |, ^, ~, <<, >> 
print(5 & 3) #bitwise and compares bitvalues of 5 and 3 and returns a value where both bits are 1. in this case 5 is 0101 and 3 is 0011 so the result is 0001 whivs is 1
#note similiar to IP address and subnet mask calculations
print(5 | 3) #bitwise or needs atleast on bit to be 1 to return 1 so the result is 0101 and 0011 which is 0111 = 7
print(6 ^ 3) #bitwise xor returns 1 if bits are different if both are 1 or 0 it returns 0 so 6 is 0110 and 3 is 0011 so diff is 0101

#when it comes to operator precedence, parentheses have highest precedence then exponentiation, multiplication, division, modulus and floor division
#more about the precedence order: https://www.w3schools.com/python/python_operators_precedence.asp

print("PYTHON LISTS: ")
#i've already used lists in examples but lets go through more deeply and figure out what is difference between lists, tuples, sets and dictionaries.
#so typical list stores multiple items in single variable. they are ordered, changeable and allow duplicate values.
mylist = ["banana", "kiwi", "strawberry"]
print(mylist)
#items in list has index values starting from [0], [1], [2] and so on. if we want to start end of the list we can use negative indexing like [-1] and so on.
print(mylist[0])
print(mylist[-1])
#since list is indexed it can contain same value multiple times.
#to see number of items in list we can check it with len() function:
print(len(mylist))
#lists can also contain any datatypes, lits are its own datatype in python for example
mylist2 = ["apple", 1, True, "banana", 3.14, mylist]
print(mylist2)
print(type(mylist2))
#you can also use list constructor to make list
mylist3 = list(("apple", "mango", "cherry"))
print(mylist3)
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. but you can remove and add items
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
#you can also slice lists like we did earlier with strings and string formats
mylist4 = ["horse", "dog", "cat", "moose", "reindeer", "fly", "whale", "bird"]
print(mylist4[2:5]) #check range from 2 to 5 but 5 is not included so it should show cat -> reindeer
#same as before if we leave starting value empty it begins from the first index of the list
print(mylist4[:4])
#and other way around. we can set starting index  and leave rest empty to fo from that index till the end of the list items
print(mylist4[3:])
#and works same way with the negatives - from starting the end of the list
print(mylist4[-4:-1])
#also can check in and not in if the value is in the list
if "horse" in mylist4:
   print("yup 'horse' is in the list")

print(mylist4)
print("changing list values of items: ")
mylist4[3] = "crocodile"
print(mylist4)
mylist4[1:3] = ["seagul", "ant"]
print(mylist4)
mylist4[1:2] = ["bear", "pig", "lion"] #if you add more items than you are replacing it will add them automatically in the list increasing lengt of the list
print(mylist4)
#if we want to add values without replacing we can use insert() method
mylist4.insert(3, "Eagle")
print(mylist4)

#adding items to the end of the list using append() method
mylist4.append("wolf")
print(mylist4)
#if we want to add elemets from another list to another, there is extend() method
mylist.extend(mylist3)
print(mylist)
#extend method does not haveto append lists, it can be any iterable object like tuplets,  sets, dictionaries etc.
mytuple = ("blueberry", "dragonfruit")
mylist.extend(mytuple)
print(mylist)

#removing items
print("removing items from list: ")