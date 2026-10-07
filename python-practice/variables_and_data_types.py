'''
-Must start with a letter (a-z, A-Z) or an underscore. 
 Cannot Start with a Number. 
 Case-Sensitive: age, Age, and AGE are three distinct variables.
 No Reserved Keywords: Cannot use Python's built-in keywords (e.g., class, def, if, import, for).
-Experienced Python developers follow snake_case for variable and function names (e.g., my_variable, calculate_sum).
-Before Python 3.6 introduced f-strings, string formatting relied on % formatting or the .format() 
 method, both of which were verbose, hard to read, and error-prone when handling multiple variables.
 F-strings solved readability issues by putting expressions directly where they appear in the final output string and improved
 execution speed over older methods.
 -In the calculation (birth_year = current_year - age), both current_year (datetime.now().year) and age are integers, hence 
 birth_year will end up as an int.
'''
from datetime import datetime
name = "Boateng Godfred Agyemang"
age = 18

current_year = datetime.now().year

birth_year = current_year - age
print(f"My name is {name.upper()} and I was born around {birth_year}, so I'm {age} years old.")

website = "www.google.com"
clean_website = website.removeprefix("www.")
print(clean_website)

a, b, c = 3, 5, 7
print("Sum:", a + b + c)

print("a^5:", a ** 5)
print("b^5:", b ** 5)
print("c^5:", c ** 5)

greeting = "welcome to hotel transylvania".title()
print(greeting)

