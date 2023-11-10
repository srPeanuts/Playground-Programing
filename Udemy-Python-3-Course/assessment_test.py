
# Q: Numbers:
# A: Numbers can be integers 1, -1, 0 or floating points 1.0, 0.0, -1.0;

# Q: Strings:
# A: Strings are basically text information or a sequence of letters and can contain numbers also. Can be created with single or double quotes. Strings are not mutable; "Ordered sequence of characters";

# Q: Lists:
# A: Lists unlike strings, they are mutable, meaning we can change the values inside lists with indexing. Lists are created with [];

# Q: Tuples:
# A: Tuples are also very similar to lists, however, they are immutable. Tuples are created with ();

# Q: Dictionaries:
# A: Dictionaries are maps, meaning they are collections of objects/information stored by keys and values unordered;


#____________Numbers__________________________________________________________________________

# Q: Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# A: 
(((((100.25 - 80.25)/2)*1000)**0.5)+0.25)


# What is the value of the expression 4 * (6 + 5) = 44
# What is the value of the expression 4 * 6 + 5 = 29
# What is the value of the expression 4 + 6 * 5 = 34

# Q: What is the type of the result of the expression 3 + 1.5 + 4?
# A: floating point and it is 8.5

# Q: What would you use to find a number’s square root, as well as its square?
# A: Square root: you use x**0.5, where is is any number you want to know the square root
# A: Square: you use ** to find the square of any given number


#_____________Strings________________________________________________________________________

# Q: Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
s[1]  # 'e'

# Q: Reverse the string 'hello' using slicing:
s[::-1] # 'olleh

# Q: Given the string hello, give two methods of producing the letter 'o' using indexing.
# 1#
s[-1] # 'o'
# 2#
s[4] # 'o'


#___________Lists___________________________________________________________________________

# Q: Build this list [0,0,0] two separate ways.
# Method 1:
l = [0]*3

# Method 2:
lf = [0,0,0]

# Q: Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'

# Q: Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()


#___________Dictionaries____________________________________________________________________

# Q: Using keys and indexing, grab the 'hello' from the following dictionaries:
a = {'simple_key':'hello'}
b = {'k1':{'k2':'hello'}}
c = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

# A:
a['simple_key']
b['k1']['k2']
c['k1'][0]['nest_key'][1][0]
d['k1'][2]['k2'][1]['tough'][2][0]

# Q: Can you sort a dictionary? Why or why not?
# A: No, because the dictionary consistes on keys and values, so they have no need to be sorted 


#___________Tuples____________________________________________________________________________

# Q: What is the major difference between tuples and lists?
# A: The big difference is that tuples are immutable.

# Q: How do you create a tuple?
t = tuple
tp = ()

#___________Sets______________________________________________________________________________


# Q: What is unique about a set?
# A: Sets are lists of unique values, they dont allow duplicate items

# Q: Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)


#___________Booleans________________________________________________________________________

# Q: 2 > 3
# A: False

# Q: 3 <= 2
# A: False

# Q: 3 == 2.0
# A: False

# Q: 3.0 == 3
# A: True

# Q: 4**0.5 != 2
# A: False

# Q: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']    # A: 3 >= 4 » False