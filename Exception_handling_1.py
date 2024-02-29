a = 10
b = 0

try:
   d =  a/b
   print(d)
   print("Inside Try")

except ZeroDivisionError as obj:               # exception is occured then run this 
#    print("Devision by zero is not Allowed")
    print(obj)   # description of exception 

else:                           # if exception does not occure then run else other wise is not run
   print('Inside else')

finally:                         # this run always if exception occurre or not
   print('Inside finally')

print("Rest of the code")
