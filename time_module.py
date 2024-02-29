from time import time , ctime , localtime

epoch = time()
print(epoch)
print()

et = ctime(epoch)
print(et)
print()

print(ctime())
print()

stobj= localtime()   # it return one object
print(stobj)
print()

print("year:",stobj.tm_year)
print("month:",stobj.tm_mon)
print("Date:",stobj.tm_mday)
print("hour:",stobj.tm_hour)
print("minutes:",stobj.tm_min)
print("second:",stobj.tm_sec)
print()

print(stobj.tm_mday,end="/")
print(stobj.tm_mon,end="/")
print(stobj.tm_year)
print()

print(stobj.tm_hour,end=":")
print(stobj.tm_min,end=":")
print(stobj.tm_sec)
