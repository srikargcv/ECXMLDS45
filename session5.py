
# Operators

# Python operators

num1 = 10 
num2 = 20

# 1. Arthimetic operator

# Used to perform common math operations

# + - Addition - A+B
add = num1 + num2

# - - Subtraction - A-B
sub = num1 - num2

# * - Multiplication - A*B
mult = num1 * num2

# / - Division - A/B
div = num1 / num2

# % - Moudlus - A%B
mod = num1 % num2

# ** - Exponentation - A**B
exp = num1 ** 2

# // - Floor Division - A//B
fd = num2 // num1

# Multiline comments / multi line String
print(f"""
The addition of {num1} and {num2} is {add}
The subtraction of {num1} and {num2} is {sub}
The product of {num1} and {num2} is {mult}
The division of {num1} and {num2} is {div}
The modulus of {num1} and {num2} is {mod}
The Power result of {num1} and {num2} is {exp}
The floor division of {num1} and {num2} is {fd}
""")

# String - "asdfasdf"  // 'afdsfasdf'

# Multi line string - """dasfadsf""" // ''' awdsfasdfadsf '''


# 2. Assignment operator

# Used to assign values to a variable

# = -> a = 5
# += -> a = a + 10 -> a += 10
# -= -> a -= 10
# *= -- /=
# :=  --> print(x := 10)

# print(x := 10)
# print(f'The value stored inside x is {x}')


# 3. Comaprision operator - Gives out a boolean value as the result

# Used to compare two values

# == - Equal - x == y
eq = num1 == num2

# != - Not equal  - x != y
eq1 = num1 != num2

# > - greater than - x > y
eq2 = num1 > num2

# < - less than - x < y
eq3 = num1 < num2

# >= Greater than or equal to - x >= y
eq4 = num1 >= num2

# <= Less than or equal to - x <= y
eq5 = num1 <=num2

print(f"""
{eq}
{eq1}
{eq2}
{eq3}
{eq4}
{eq5}
"""
)


# 4. Logical operator

# Used to combine conditional statements

# a = 10
# b = 20
# c = 30

# x - a > b - False
# y - c > b - True


# and - x and y -> False
# or - x or y -> True
# not - not(x) - True  -- not(y) - False

# Identity operators

# used to comapre the objects - if they are actually same
# is 
# is not


# Membership operator

# used to test if a sequence is presented in the object
#  in
#  not in

# Bitwise operator

# used to perform binary operations

# & - AND

tv1 = True
tv2 = False

ftv1 = tv1 & tv2
ftv2 = tv1 | tv2
print(ftv1)
print(ftv2)
# | - OR
# ^ - XOR
# ~ - NOT

# >> - Zero left shift
# << - Signed rioght shift 

# Task

# write up new variables wehre you can check the Intrest rate of a give time period and IV and principal amount