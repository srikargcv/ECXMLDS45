
# Variables and also types of variables

# String - String is actually a sequence of chars - Letters, spaces, Symbols, enclose them in quotes

# String - Immutable 
# But we can create new strings based on operations - String methods - String Manipulations

# Example :

student_name = "nAgeNdrA"  #Lower case alphabets

# 1. lower() - Convert the string into Lowercase

name_lowercase = student_name.lower()

print(f'The lowercase of the {student_name} is {name_lowercase}')

# 2. upper() - Convert the string into uppercase

name_uppercase = student_name.upper()

print(f'The uppercase of the {student_name} is {name_uppercase}')

# 3. Capitalize - First charecter of the string will be capitalise / will be converted to upper case

name_capitalize = student_name.capitalize()

print(f'The Capitalization of the {student_name} is {name_capitalize}')

# 4. Title() - First charecter of every word in the string will be capitalised / will be converted to upper case

string2 = "hEllo IaM NagEnDra"

string2_title = string2.title()

print(f'The Title  is {string2_title}')


# len() - Getting the length of the String

print(len(string2))

# 5. strip() - Remove the space from ends

name = "     Nagendra   "

print(name)
print(name.strip())

# 6. replace() - To replace a set of chars inside a string

message = "Hello Iam ABCD"

print(message.replace("ABCD",'Nagendra'))



# Dont use any loops or any condition flow 

# Create a String with multiple methods which will print out User name, Full name Password with *

# 123456789 - ********



# "Helllo my name is XYZ, My user name is ABCD, Your password is ******** , my mail address is pqrs@gmail.com"