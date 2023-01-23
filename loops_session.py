# FOR

numbers = [1, 2, 3 ,4 ,5 ,6, 7, 8 ,9]
items = ['ball', 'car', 'bird']

for number in numbers:
    print(number)

print("Operates:")
print("A- Break:")
# Operates:
#    1- Break:
for num in numbers:
    if num == 4:
        break
    print(num)


#    2- Continue:
print("B- Continue:")
for num in numbers:
    if num == 7:
        continue
    print(num)

# Parent(Main) and Child(Sub) Loops
for num in numbers:
    for item in items:
        print(num, item)

# Loop in a numeric range:
# result must be: 0 to 9
for ii in range(10): 
   print(ii)

print('++++======++++')
# result must be: 1 to 9
for ii in range(1,10): 
   print(ii)


# WHILE

x = 5
while x < 60:
    print(x)
    x = x + 5 

print('++++=== with a break ===++++')
# with a break
while x < 80:
    print(x)
    if x == 75:
       print('yoohoo')
       break
    x+=5
