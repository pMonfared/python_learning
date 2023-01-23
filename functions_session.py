
car_colors = {1: 'blue', 2: 'green', 3: 'white', 4: 'black'}

# Void functions
def car_color_print():
   print('Car Color')


# Return functions
def car_color_print_with_return():
   message = 'car color'
   return message


msg = car_color_print_with_return()
print(msg)

# Return function with input required arguments
def car_color_print(num):
    car_color = car_colors[num]
    message = f'car color: {car_color}'
    return message


print(car_color_print(3))

# Return function with input required and optional arguments
def car_color_print(num, input_text = 'Hello'):
    car_color = car_colors[num]
    message = f'{input_text}, car color: {car_color}'
    return message

# call function just with fill the required parameters
print(car_color_print(4)) 
# call function with fill the required and optional parameters
print(car_color_print(4,"I put my text Haha!"))



# * and ** 
def car_info(*args, **kwargs):
    print(args)
    print(kwargs)

car_info('Tehran', 'Paris', brand='Ford', model='Mustang')


cities = ['Tehran', 'Paris']
specs = {'brand':'Ford', 'model':'Mustang'}


car_info(cities, specs)
# VS
car_info(*cities, **specs)