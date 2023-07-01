"""
Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple

"""
dummy_var = "pw data science" # variable conatains str type of data
print(dummy_var) # output- pw data science

dummy_var = [10,20, 'dummy', [20], 20] # contains list type of data 
print(dummy_var) # [10,20, 'dummy', [20], 20]

dummy_var = 20.44 # conatains float type of data
print(dummy_var) # 20.44

dummy_var = (10,20,30,20,"pw",'data science') # contains tuple type of data
print(dummy_var) # (10,20,30,20,"pw",'data science')

"""
Q2. Given are some following variables containing data:
(i) var1 = ‘ ‘
(ii) var2 = ‘[ DS , ML , Python]’
(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
(iv) var4 = 1.
What will be the data type of the above given variable.

"""
var1= ' '
var2= '[ DS , ML , Python]'
var3= [ 'DS' , 'ML' , 'Python']
var4= 1.
print(f"var1 type -> {type(var1)}") # var1 type -> <class 'str'>
print(f"var2 type -> {type(var2)}") # var2 type -> <class 'str'>
print(f"var3 type -> {type(var3)}") # var3 type -> <class 'list'>
print(f"var4 type -> {type(var4)}") # var4 type -> <class 'float'>

"""
Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **
"""
num_one = 10
num_two = 5
print(f"num_one / num_two = {num_one / num_two}") # num_one / num_two =  2.0 ('/' operator performs floating-point division)
print(f"num_one % num_two = {num_one % num_two}") # num_one % num_two =  0 ('%' operator retun remainder )
print(f"num_one // num_two = {num_one // num_two}") # num_one // num_two =  2 ('//' operator performs integer division )
print(f"num_one // num_two = {num_one ** num_two}") # num_one ** num_two = 100000 ('**' operator performs power i.e 10*10*10*10*10)

""" 
Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type. 
"""
dummy_list = [
    10,
    "pw",
    20.3,
    20+2j,
    ('abc', 'cdf'),
    {'name': 'pw data science', 'cost': 3500},
    {10,20,20,30},
    True,
    [20,40,80],
    range(1,5)
]
for x in dummy_list:
    print(f"{x} and type is {type(x)}")
'''
output 
10 and type is <class 'int'>
pw and type is <class 'str'>
20.3 and type is <class 'float'>
(20+2j) and type is <class 'complex'>
('abc', 'cdf') and type is <class 'tuple'>
{'name': 'pw data science', 'cost': 3500} and type is <class 'dict'>
{10, 20, 30} and type is <class 'set'>
True and type is <class 'bool'>
[20, 40, 80] and type is <class 'list'>
range(1, 5) and type is <class 'range'>
'''

"""
Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.
"""

num_one = int(input("enter first number ").strip())
num_two = int(input("enter second number ").strip())
count=0
while(num_one % num_two == 0):
    num_one = num_one // num_two
    count += 1
print(f" num_one // num_two count {count}")

# output 
# num_one = 21 num_two= 3 
# num_one // num_two count 1 

""" 
Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.
"""
dummy_int_list = list(range(1,26))
for x in dummy_int_list:
    if (x % 3 == 0):
        print(f"element {x} is divisiable by 3")
    else:
        print(f"element {x} is not divisiable by 3")

"""
Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.
"""

# immutable means can't change values once they are created 
name = "pw data science"
modify_name = name.title()
print(modify_name) # Pw data science
print(name) # pw data science
tuple = (10,20)
modify_tuple = tuple + (40,50)
print(tuple) # (10,20)
print(modify_tuple) # (10,20,40,50)

# mutable means can change values once they are created 
list= [10,20]
print(list) # [10,20]
list.append(50)
print(list) # [10,20,50]
