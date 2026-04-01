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
print("data types: \n")
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
print("datatype conversions: \n")
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
print("multilines and strings: \n")
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
print("modifying strings: \n")
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
print("\n boolean values: \n")
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
print("arithmetic operators: \n")
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
print("assigment operators: \n")
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

print("comparison operators: \n")
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

print("logical operators: \n")
# and, or and not also
a = 5
print(a > 3 and a < 10) #should be true
print(a > 3 or a < 4)  #should be true only one of the conditions needs to be true
print(not(a > 3 and a < 10)) #should be false because normal codition is true but we negate it with not so it returns false

print("identity operators: \n")
#identity opreators is and is not compare memory locations of two objects adn returns true if the are the same
#note value is not same as identity, two different objects can have same value but they are not the same object in memory
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x == y) #this is true because == compares values of x and y
print(x is y) #this is false because they are different objecrs in memory
print(x is not y) #true
z = y
print(z is y) #true because z and y are same object in memory

print("membership operators: \n")
#in and not in are used to test if a sequence is present in object
x = ["apple", "banana", "cherry"]
print("banana" in x) #returns true because banana is in list x
print("grape" in x) #returns false
print("banana" not in x) # false because it is in x
print("grape" not in x) #true
#membership operators work also in strings and you can check if certain character or phrase is in or is not in string

print("bitwise operators: \n")
# bitwise operators are used to compare binary numbers, they are &, |, ^, ~, <<, >> 
print(5 & 3) #bitwise and compares bitvalues of 5 and 3 and returns a value where both bits are 1. in this case 5 is 0101 and 3 is 0011 so the result is 0001 whivs is 1
#note similiar to IP address and subnet mask calculations
print(5 | 3) #bitwise or needs atleast on bit to be 1 to return 1 so the result is 0101 and 0011 which is 0111 = 7
print(6 ^ 3) #bitwise xor returns 1 if bits are different if both are 1 or 0 it returns 0 so 6 is 0110 and 3 is 0011 so diff is 0101

#when it comes to operator precedence, parentheses have highest precedence then exponentiation, multiplication, division, modulus and floor division
#more about the precedence order: https://www.w3schools.com/python/python_operators_precedence.asp

print("\n PYTHON LISTS:  \n")
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
print("changing list values of items:  \n")
mylist4[3] = "crocodile" #replces
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

#removing items from lists can be done using remove() method remove method removes first item with specified value if there happens to be dublicates
print("removing items from list: ")

mylist.remove("blueberry")
print(mylist)
 # but if you want to remove by index from the list you can use pop() method

mylist.pop(1)
print(mylist)

#you can also use del keyword to delete specified index with del mylisy[0] or just delete whole list with: del mylist
#then there is also clear() method which empties the entire list content. list itself still remains

print("Looping through list: ")
# lets use for loop to go through mylist until it reaches the end of the list and use membership operator in to check the items inside mylist
for x in mylist:
   print(x)

print("looping using index numbers: ")
#if we want to go through by index number use range() and len() functions
for i in range(len(mylist)):
   print(mylist[i])
#so here we for loop like earlier through the list but we use the range() and len() to determine how many items are in the list.
#to open up it more how the loop works lets print the len(mylist) to show first how many items are in the list and then go thgough range of that length
print(len(mylist))
print(range(len(mylist)))

print("looping list with while loop: ")
#using while loop lets use len() again to list amount of items in list but we also have to have variable that starts from the beginning
i = 0
while i < len(mylist):
   print(mylist[i])
   i = i + 1
#here we first set variable i to 0 and while the value of i is less than the lenght of the list index which is 6 in this case while loop keeps printing
#the list until it reaches the point where i >= lenght of the list because the statement does not fullfill anymore. so each time while loops we add 1 to i
#until it the statemet does not work anymore

print("looping list with list comprehension: ")
#list comprehension loop is shorter version of the for loop method that prints all items in list, it works like this:
[print(x) for x in mylist]
#i'd say that list comprehension is useful to make oneliners. so these things are same thing but without list comprehension and with
print("creating list animals withour and with list comprehension: ")

animals = ["dog", "cat", "bear", "fish", "tiger"]
newanimals = []

for x in animals:
   if "i" in x:
      newanimals.append(x)

print(newanimals)

#with list comprehension
foods = ["spaghetti", "carbonara", "soup", "pizza", "hamburger"]
newfoods = [x for x in foods if "i" in x] #so here newfoods list = x and we for loop x in foods list and if letter "i" is in the x (looped foods items) it is the x in newfoods list

print(newfoods)
#note comprehension is more efficient also in bytelevel because python does not need to roll through append for every time. here it is just automatically added in new list x value if it passes the statement
#can use other operatos aswell in the statemnt for example [x for x in foods if x != "spaghetti"] here all other than spaghetti will be added to new list
#also obviously dont need to have statements in the oneliner, can just create newlist from existin one with newlist = [x for x in oldlist]

rangelist = [x for x in range(10)]
print(rangelist)

rangelist2 = [x for x in range(10) if x < 5] #adds numbers in range to list if they are less than 5
print(rangelist2)

#we can do pretty much anything with the values for the new lists with comprehensions
foods2 = [x.upper() for x in foods] #here we just make uppcase letters list from the foods list
print(foods2)

foods3 = ["food" for x in foods] #here we make all items from foods list to say "food" in this new list
print(foods3)

foods4 = [x if x != "soup" else "stew" for x in foods] # here we manipulate the list to return stew instead of soup from the list foods to this new list
print(foods4)

print("Sorting lists: ")
#lists can be sorted using sort() method
foods.sort()
print(foods)
numberslist = [900, 699, 10, 65, 99, 49, 3, 0] #works with numbers aswell
numberslist.sort()
print(numberslist)

#and if we want sort in reverse order use reverse = True
numberslist.sort(reverse = True)
print(numberslist)

def numbersfunc(n): #in this function we set variable n and return rule to closest to 50 then we sort using keyword argument and this function
   return abs(n - 50)

numberslist.sort(key = numbersfunc)
print(numberslist)

#note sortihg list that has case sensitive values the sort itself sorts capital letters first then lower but this can be fixed using key function
casesensitivelist = ["Beta", "alfa", "foxtrot", "Charlie", "Echo"]
casesensitivelist.sort()
print(casesensitivelist)

casesensitivelist.sort(key = str.lower) #str.lower does the trick
print(casesensitivelist)

casesensitivelist.reverse()
print(casesensitivelist)

print("COPYING LISTS \n")
#note use copy() method to copy contents of a list rather than refering to another list or variable because those values can change and copied values will we changed aswell

copiedlist = fruits.copy()
print(copiedlist)
#also using list() method will also copy the contents of pointed thing
copiedlist2 = list(foods)
print(copiedlist2)
#also previously used slice operator can be used to copy items
copiedlist3 = numberslist[:] #but we are not slicing anything here we are starting from the beginning and ending to numberslist end therefore we copy all
print(copiedlist3)

print("JOIN LISTS \n")
#we can join or concatenate lists for example
joinlistx = ["a", "b", "c", "d"]
joinlisty = [1, 2, 3, 4, 5]
joinlist = joinlistx + joinlisty
print(joinlist)

#using append to join lists
for x in joinlisty:
   joinlistx.append(x)

print(joinlistx)

joinlistx.extend(joinlisty) #extend also can be used to concatenate lists
print(joinlistx)

"""
list of build-in methods we just used in lists
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

print("\n TUPLES \n")
#tuples are similiar to lists and has pretty much same funtions as lists but they differ that tuples are collection of items which are ordered and unchanheable
#unlike lists are changeable
#same index numbering, allows duplicate values inside tuple
numbertuple = (14, 16, 90, 504)
print(len(numbertuple)) #len() method prints amount of indexes
#tuples can also contain any datatypes
print(type(numbertuple)) #tuple is its own datatype
fruittuple = tuple(("orange", "apple", "cherry"))
print(fruittuple) #like lists you can use tuple() constructor to create new tuple
#note since tuples are unchageable it means contains of tuple can not be changed like removing or adding.
#same as in lists we can use keyword in to check is something is present
if "apple" in fruittuple:
   print("Yes 'apple' is in fruittuple")

print("\n Tuple workarounds \n") 

y = list(fruittuple) #converting tuple in to a list and adding value to it and then converting list back to tuple
y[1] = "kiwi"
y.append("melon")  #append adds end of the list
fruittuple = tuple(y)

print(fruittuple)
#can also add tuples to tuples basically we are not adding values in tuple. we are just adding tuple to another tuple
z = ("starberry",)
fruittuple += z
print(fruittuple)
#removing items from tuple is not possible without workaround like converting to list and then removing
y = list(fruittuple)
y.remove("orange")
fruittuple = tuple(y)
print(fruittuple)
#deleting tuples work similiar to lists just use del keyword like this: del fruittuple <- deletes fruittuple
print("\n packing and unpacking tuples \n")
#packing and unpavking works siliar to list
#packing is basically giving values for tuple
tuplepack = ("cheese", "cucumber", "tomato") #packing

(yellow, green, red) = tuplepack #this is unpacking. we are assigning containts of tuple to variables yellow greeen adn red
print(yellow)
print(green)
print(red)

print("\n more containts in tuple than assigned variables use asterisk* ")
tuplepack2 = ("cheese", "cucumber", "tomato", "bread", "garlic")

(yellow, green, *red) = tuplepack2 #if there is more items in tuple than you have variables to assign use asterisk* to set rest of the values to variable
print(yellow)
print(green)
print(red)
#you can also give asterisk to lets say green in this case -> then first item goes to first variable yellow and last item goes to last variable red. rest is automatically on green now
print("\n looping through tuples\n")
#looping works same as in list
for x in fruittuple:
   print(x)

print("\n using range and len looping through index numbers\n")
#same goes for range() and len() if you want loop through index numbers
for i in range(len(fruittuple)):
   print(fruittuple[i])

print("\n looping with while loop")
i = 0
while i < len(fruittuple):
   print(fruittuple[i])
   i = i + 1

print("\n Join tuples similiar to lists before \n")
tuple1 = ("a", "b", "c")
tuple2 = (1, 2 ,3)

newtuple = tuple1 + tuple2
print(newtuple)
#you can multiply contents of tuple just with * operator
multiplytuple = tuple1 * 2
print(multiplytuple)

print("tuple build-in methods")
countingtuple = (1, 3, 5, 6, 7, 6, 5, 3, 2, 5, 7, 9)
x = countingtuple.count(5) #with this count() method we can check occurances that how many times number 5 appears in this tuple
print(x)

indextuple = (1, 3, 5, 2 ,3 ,2 ,7 ,8 ,6 ,5, 9)
x = indextuple.index(2) #with index() method you can check the first occurance of value and check its index in tuple
print(x)

print("\n SETS \n")

#sets are anoteher collection of data like lists and tuples. what differs is that set items are unchageable, unordered and unindexed
#note YOU CAN ADD AND REMOVE ITEMS FROM SET
#sets are written with curly brackets {}, list [], tuple ()
fruitset = {"apple", "banana", "kiwi"}
print(fruitset)
#since sets are unordered you cant be sure in which order items will show. they can show different order each time.
#sets also cant be referred by index or key since they are unindexed
#sets also ignore duplicate values because it cant have two same values
dupset = {"apple", "apple", True, 1, False, 0, 2}
print(dupset)
#as we can see set sees True and number 1 as same value therefore it does not print it since it is duplicate value same goes with False and 0
print(len(dupset)) #len prints only the amount set has so duplicates are not counted

constructedset = set(("gorilla", "cheetah", "walrus"))
print(constructedset)
print(type(constructedset))
#set can be constructed using set() method like tuples and lists also set itself is also datatype

for x in fruitset:
   print(x)
#looping works similiar to other lists and tuples

print("apple" in fruitset)
#also can use in and not in methods to check if set contains that item. you cant use indexes
print("kiwi" not in fruitset)
print("\n adding items in set \n")

#can add items in set just by using add() method
fruitset.add("orange")
print(fruitset)

#if oyu want to add items from another set into your set you can use update() method
addset = {"strawberry", "mango", "lingonberry"}

fruitset.update(addset)
print(fruitset)
#note you can use update() method to add items to set from any onther iterable objects like lists, tuples, dictionaries
#fruitset.update(fruitlist)
print("\n removing items from set \n")
fruitset.remove("mango")
print(fruitset)
#removinh items that does not exist in set gives error
#but if you use discard() method it does not give error if the item does not exist in set
fruitset.discard("lingonberry")
print(fruitset)
#if you decide using pop() method it will remove random item because you cant specify by index and items are unordered in sets
#clear() method works the same like in lists and tuplese -> removes all items from the set
#and del keyword can be used to delete the set -> del fruitset
print("\n looping throgh set gives random order because set is unordeder. \n")
for x in fruitset:
   print(x)

print("\n join sets \n")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, 4}

set3 = set1.union(set2)
print(set3)
#union() method does the same as we before used + operator to add list1 to list2
set4 = set1 | set2 #the '|' operator can also be used to join sets and it gives the same result
print(set4)
#both methods works and you can add as many as you want jointset = set1.union(set2, set3, set,4 etc.)
#or just keep piping with | operator like joinset = set1 | set2 | set3 |set4 etc.
#can also join different datatypes together but then you must use union() method because '|' operator only allows you to combine sets to sets

#even though sets are unchangeable we still can add contents in set from other sets with update() method
set1.update(set2)
print(set1)
#update method excludes duplicates aswell but with intersection() method you can keep ONLY duplcates
duplicset1 = {"apple", "banana", "orange"}
duplicset2 = {"apple", "banana", "kiwi"}
duplicsetresult = duplicset1.intersection(duplicset2)
print(duplicsetresult)

#or just use & operator. it does the same thing except with & operator you can only join sets with sets
duplicsetresult2 = duplicset1 & duplicset2
print(duplicsetresult2)
#as before we made new set with only duplicate items. if we want to just use existing set and change values to duplicate only with another set we can use
#intersection_update() method
duplicset1.intersection_update(duplicset2)
print(duplicset1)
#note if you have integers 1 and 0 values and bool values True or False those are concidered as duplicates and they will be included in your set then
#but i think True and False values goes to set over 1 and 0

# then there is difference() method that keeps items on set that are not presetn in the other set
diffset1 = {"apple", "banana", "kiwi"}
diffset2 = {"apple", "mango", "pineapple"}
diffsetresult = diffset1.difference(diffset2)
print(diffsetresult) #prints kiwi and banana
# - operator works similiar but again can be used only set - set situation
#then similiar to intersection_update() we can use difference_update() updates the chosen set instead of creating new set for difference
#diffset1.difference_update(diffset2)
#print(diffset1)

#symmetric_difference() method keeps only items that are not present in both sets
symdiffset = diffset1.symmetric_difference(diffset2)
print(symdiffset) #in these sets only apple is same in both sets so it prints banana,kiwi,mango and pineapple
# ^ operator does same thing and again can assume that it works only with set on set action
symdiffset2 = diffset1 ^ diffset2
print(symdiffset2)
# and same as before symmetric_difference_update() you can just update the set with another sets items instead of making new set
diffset1.symmetric_difference_update(diffset2)
print(diffset1)

print("\n FROZENSET \n")

#frozenset() is same as set BUT you can NOT add or remove items in frozenset()
#can make frozenset with constructor
froznset = frozenset({"apple", "banana", "cherry"})
print(froznset)
print(type(froznset))

#frozen set has some methods even though yo ucant add or remove elemets from it
frset = frozenset({1, 2, 3})
frset2 = frozenset({2, 3, 5, 6})
copyset = frset.copy()
print(frset)
print(copyset)

#difference and intersection works in frozensets aswell
print(frset.difference(frset2))
#or with - method
print(frset - frset2)

print(frset.intersection(frset2))
#there is also method that returns true or false if two frozensets have intersection -> isdisjoint()
print(frset.isdisjoint(frset2))

#then there is supset or superset checks if the frozenset is subset of another set or superset another -> <=, >=
print(frset.issubset(frset2))
#or
print(frset <= frset2) #or just use <
#or superset check
print(frset.issuperset(frset2))
#or
print(frset >= frset2) #or >
#symmetric_difference() works same as before can be used in frozensets too and same with union() method

"""
here is list of the methods in sets that we went through:
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
"""
print("\n DICTIONARIES \n")

mydict = {
   "brand": "Volvo",
   "model": "V60",
   "year": 2020,
   "year": 2025, #if you have duplicates last duplicate will overwrite the previous one like in this case year will be 2025
   "colors": ["grey", "white", "red", "green"]
}
#dictionaries use key:value pairs they are ordered, changeable and do not allow duplicates it differs from lists so you can refer to key to get the value
print(mydict["brand"]) #with key "brand we cet get the value which in this casi is "Volvo"
print(mydict)
print(len(mydict))
print(type(mydict))
#dictionaries support any datatype and can contain lists

#dicttionary can be made by using constructor dict()
newdict = dict(name = "John", age = 66, country = "Albania")
print(newdict)
# dictionaries are ordered and changeable
#we can use keys() method to get all key values in dictionary
x = mydict.keys()
print(x)
mydict["horsepower"] = 165 #we can add new key value pairs
print(x)
#just like getting all keys we can get all values of the keys using values() method
x = mydict.values()
print(x)
mydict["horsepower"] = 195
print(x) #obviously if we change the key:valu pair printed values wil change aswell

#if we want to get all info from dictionary we can use items() method to get all key:value pairs
x = mydict.items()
print(x)

#and just like in lists and tuples we can check if certain value is in the dictionary with in and not in methods
if "brand" in mydict:
   print("yup 'brand' is in mydict")

#also as we checked keys and values we can do that also with get() method
print(mydict.get("brand"))

#we can chanve values in dictionary with mydict[key] = newvalue or with update() method
mydict.update({"year": 2022})
print(mydict)

#if we want we can add items to dictionary just by giving new key and value to it like mydict["type"] = "sedan"
mydict["type"] = "sedan"
print(mydict)
#then we can revmove items just like in lists and sets with pop() method
mydict.pop("type")
print(mydict)
#and popitem() if you want to remove latest added item in the dictionary: mydict.popitem()
#then we can use del keyword to delete either specific item like: del mydict["model"] or if you want to remove whose dictionary use del mydict
#and if you want to empty the dictionarys contents use .clear() method just like in lists and sets
print("\n looping through dictionaries \n")
#we can loop through dictionary with for loop like we did in lists and tuples
for x in mydict:
   print(x)
#as we can see this loops through only keys of the dictionry. if we want to loop through values   lets print values
for x in mydict:
   print(mydict[x])
#or alternatively use values() method to loop through values
for x in mydict.values():
   print(x)
#same works with keys() method
for x in mydict.keys():
   print(x)
#and if we want to get both keys and values use items() method
print("\n loop keys and values with items method \n")
for x, y in mydict.items():
   print(x, y)

print("\n copying dictionaries \n")
#same as in lists we can copy dicts with copy() method or constructor dict()
copydict = mydict.copy()
print(copydict)
copydict2 = dict(mydict)
print(copydict2)

print("\n nested dictionaries \n")