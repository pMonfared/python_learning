

# List are mutable (قابل تغییر اند)

colors = [ 'red', 'blue', 'green']
numbers = [4, 8, 23, 56, 2]
colors_2 = ['white', 'black']

#empty list
list_1 = []
list_2 = list()


print("Numbers:")
print(numbers[1:5])

print("Colors:")
print(colors)


# add an element end of a list
colors.append('orange')
print(colors)

# add an element to a list in specific index
colors.insert(1,'pink')
print(colors)


#change an element value by select specific index number
colors[1] = "silver"

# add a list to another list
colors.extend(colors_2)
print(colors)

# remove the latest element of list
popped_item = colors.pop()
print(colors)
print(popped_item, "<= removed from the Colors")


# sort numbers elements => Min to Max amount <= This operate maybe doesn't work as well
numbers.reverse()
print(numbers)


# sort numbers elements =>  Min to Max amount
numbers.sort(reverse= True)
print(numbers)

# sort numbers elements => Max to Min amount
numbers.sort()
print(numbers)


# put sorted Colors elements to another variable cause I don't want change in the Colors list
colors_sorted = sorted(colors)
print("colors:",colors)
print("colors_sorted:",colors_sorted)


# check specific element exist in the list or not
print('green' in colors)
print('purple' in colors)
print(23 in numbers)

# print element's index and element in a loop
for index, color in enumerate(colors):
    print(index, color)


# join list to a string by using specific char
colors_splitted = ' | '.join(colors)
print(colors_splitted)

# split element by a specific char to a list
message = colors_splitted #'red | pink | blue | green | orange | white'
colors_joined = message.split(' | ')
print(colors_joined)



# Tuples are immutable (غیرقابل تغییر اند)

# empty tuple
tuple_1= ()
tuple_2= tuple()

colors_tup = ('red', 'blue', 'green')
print(type(colors_tup))
print(len(colors_tup))
print(colors_tup.index('blue'))


# Set => will not show duplicate elements

#empty set
set_1 = {}  # !important => this a empty variable as dictionary not a set, so we can't create an empty set like this
set_2 = set()

colors_set1 = { 'red', 'blue', 'green', 'white'}
colors_set2 = { 'blue', 'green', 'white', 'organe', 'black'}

# union (اجتماع دو مجموعه)
print(colors_set1.union(colors_set2))
# intersection (اشتراک دو مجموعه)
print(colors_set1.intersection(colors_set2))
# difference (تفاوت مجموعه اول با مجموعه دوم)
print(colors_set1.difference(colors_set2))
# difference (تفاوت مجموعه دوم با مجموعه اول)
print(colors_set2.difference(colors_set1))


numbers_as_list = [2,4,54,43,4,8,53,54,4,2]
numbers_as_set = set(numbers_as_list)

print(numbers_as_list)
print(numbers_as_set)