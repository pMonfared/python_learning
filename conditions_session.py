#IF

teacher = 'Maryam'
student = 'Pooria'
language = 'Python'
Online = True
x = 15
y = 21

# Condition 1
if teacher == 'Maryam' :
    print(f'Yes, {teacher} is Python teacher')
else:
    print("No, I don't know anyone else!")


# Condition 2
if teacher == 'Pooria' :
    print('Yes she is Python teacher')
else:
    print("No, Pooria isn't Python teacher, But maybe in the future he can teach others!")\

# Condition 3 (And)
if student == 'Pooria' and teacher == 'Maryam':
    print('Yes, Maryam teaches Python and Pooria is his student!')
else:
    print("I don't know!")

# Condition 3 (Or)
if student == 'Pooria' or teacher == 'John':
    print('John is not a teacher but Pooria is a student!')
else:
    print("I don't know!")

# Condition 4 (Complex)
if (student == 'Pooria' or teacher == 'John') and language == 'Python':
    print('John is not a teacher but Pooria is a student! and Python is a programming languages')
else:
    print("I don't know!")

z = 349

# Condition 5 (Multiple)
if z < 300:
    print('Z isn\'t greater than 300' )
elif 300 < z < 350:
    print("Z is between 300 to 350")
elif 350 < z < 400:
    print("Z is between 350 to 400")
else:
    print("Z is Z! :)")


# Comperaisons:

# Equal
print("x Equal 2:")
if x == 2:
    print('Yes')
else:
    print('No!')

# Not Equal

print("x Not Equal 10:")
if x != 10:
    print('Yes')
else:
    print('No!')

# Greater than
print("x Greater than x:")
if y > x:
    print('Yes')
else:
    print('No!')

# Less than
print("x Less than 3:")
if x > 3:
    print('Yes')
else:
    print('No!')

# Greater or Equal
print("y Greater or Equal 10:")
if y >= 10:
    print('Yes')
else:
    print('No!')

# Less or Equal
print("y less or Equal 10:")
comperaison = y <= 10
if comperaison == True:
    print('Yes')
else:
    print('No!')

# Object Identity: is

w = x
j = 15
print('w equal x', w == x)
print('w is x', w is x)

print('j equal x', j == x)
print('j is x', j is x)

print(id(x))
print(id(j))


# Note:
# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For exmaple, '', (), [] .
# Any empty mapping. For exmaple, {} .


# case sensitive
if student == 'pooria':
    print('doroste')
else:
    print('ghalate')

if student.lower() == 'pooria':
    print('doroste')
else:
    print('ghalate')