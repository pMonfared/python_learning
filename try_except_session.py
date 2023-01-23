

# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass


text = input("Your age:")

# try:
#     print("Your age is ", str(int(text)))
# except:
#     print("Not a number")
# else:
#     print("Thank you!")
# finally:
#     print('Bye!')



# Handle several different expections

txtfilename = 'text_file.txt'

try:
    f = open(txtfilename)
    print("Your age is ", str(int(text)))
except FileNotFoundError:
    print('Filename not correct')
except ValueError:
    print("text must be integer")
except Exception as e:
    print(e)
else:
    print(f.read())
    print("Thank you!")
finally:
    print('Bye Bye!')
    
try:
    f.close()
except:
    pass  # doesn't matter if return any expection
