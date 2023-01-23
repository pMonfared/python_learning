
car = {'brand': 'Ford', 'Model': 'Mustang', 'year': 1965, 'colors': ['red', 'blue', 'black']}
       # Key  :  Value,  Key   :  Value , etc.

# get a key's value

print(car['brand'])

# There is a issue in abow line and that is if the key doesn't exist in the car dictionary
# the app will return an expection
# so if you want to resolve this issue or handle kind of these expection
# you can use this alternative :

print(car.get('city', "city as a key doesn't exist"))


# update a key: value to dictionary
car['year']= 1970
print(car)

# add a key: value to dictionary
car['city'] = 'Tehran'
print(car)

# update multiple key: value to dictionary
car.update({'brand':'Chevrolet', 'Model':'Corvette', 'year': 1963})
print(car)


# delete a key: value from dictionary
del car['Model']
brand = car.pop('brand')
print(car)

# get dictionary keys
print(car.keys())

# get dictionary values
print(car.values())

# get dictionary keys:values as odds
print(car.items())

# shows key:value prettier by use a loop
for key , value in car.items():
    print(key, " --- ", value)