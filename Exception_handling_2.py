a = 10
b = 5

try:
    d = a/g
    # d = a/b


except (ZeroDivisionError,NameError) as obj:   #This is using tuple for more than one exception handles
    print(obj)

# except (ZeroDivisionError,NameError) :
#     print('Exception handler')

# except ZeroDivisionError as obj:
#     print(obj)

# except NameError as ob:
#     print(ob)

print('Rest of the code')