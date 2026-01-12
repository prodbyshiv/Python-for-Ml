

# Rules for naming variables
"""
Module: basics.py
Purpose: Demonstrates fundamental Python concepts including variable naming, 
         data types, type casting, lists, dictionaries, and conditional statements.

Key Concepts Covered:
    - Variable naming conventions and assignment
    - Type casting using int(), float(), and str()
    - List operations (indexing, slicing, adding, removing elements)
    - List utility functions (len, sum, max, min, sort, reverse)
    - Dictionary creation and modification with key-value pairs
    - Conditional statements (if, elif, else)

Why Convert to int()?
    Converting to int() is necessary when:
    1. You have a string representation of a number (e.g., "10") and need to 
       perform mathematical operations on it
    2. User input from input() returns a string by default, but you need 
       numeric values for calculations or comparisons
    3. You need to ensure type consistency for operations that require integers
    4. To avoid TypeError when performing arithmetic or comparison operations 
       on string types
    
    Example: int("10") converts the string "10" to integer 10, allowing 
             mathematical operations instead of string concatenation.
"""
"""age = 21
_colour = "lilac"
total_score = 90

#assigning values to variables
x = 5
x = "aarya"
y = 3.14
z = "hi"
print(x)

#Assigning the Same Value
a = b = c =100
print(a,b,c)

#Assigning Different Values
x,y,z = 1,2.4," Deep Jandu"
print(x,y,z)

#Basic Casting Functions
#int(): Converts compatible values to an integer.
#float(): Transforms values into floating-point numbers.
#str(): Converts any data type into a string.

s = "10"
n = int(s)
cnt = 5
f = float(cnt)

#list in python

numbers = [10,20,30,40]
# Access list elements by index (0-based)
# print(numbers[0])  # First element: 10
# print(numbers[1])  # Second element: 20
# print(numbers[2])  # Third element: 30
# print(numbers[3])  # Fourth element: 40

# Access list elements using negative indices (from the end)
# print(numbers[-1])  # Last element: 40
# print(numbers[-2])  # Second to last element: 30

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]

# Add elements
numbers.append(60)       # end me add
numbers.insert(2, 15)    # index pe add
print(numbers)

#Remove elements
numbers.remove(30)   # value se remove
numbers.pop()        # last element remove
numbers.pop(1)       # index se remove

# Function    Use
# len()       length
# sum()       total
# max()       max value
# min()       min value
# sort()      sort
# reverse()   reverse

length_of_numbers = len(numbers)
totalSum = sum(numbers)
print(totalSum)

#What is a Dictionary?

#A dictionary stores data in key : value pairs.
params = {
    "learning_rate": 0.01,
    "epochs": 100,
    "batch_size": 32,
    "optimizer": "adam"
}

params["learning_rate"] = 0.009
print(params)

# if else 
user_marks = int(input("enter your marks: "))


if user_marks >= 40:
    print("Pass")
elif user_marks < 40:
    print("maa chudao")
else:
    print("C")

   #and / or (IMPORTANT) 

accuracy = float(input("enter accuracy"))
loss = float(input("enter loss"))

if accuracy > 0.8 and loss < 0.2:
    print("eligible")

# for loops in python
"""

"""data = [10,20,30]
for i in data: 
    print(i)"""

# range(start, end, step)
#for i in range(1, 10, 2):
   # print(i) 

   # range(start, end, step)
"""numbers = [1,2,3,4,5]
for n in numbers: 
    if n % 2 == 0:
        print(n, "even hai laude")
    else:
        print( n, "odd hai sir")"""

phone = {
    "brand" : "Ramsung",
    "price" : "₹69,000"
}
# for x, y in phone.items():
#     print (x,"->",y)

#     items = [2,3,2,1,2]
#     for i in items:
#         print(i+1)

"""        🔹 Function ka structure (dimag me bithao)
def function_name(input):
    kaam
    return output"""






def remove_duplicates(nums):
    if not nums: 
        return 0

    i = 0

    for j in range (1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] # Note: Input must be sorted for this logic
length = remove_duplicates(nums)

print(f"New length: {length}")
print(f"Modified list: {nums[:length]}")