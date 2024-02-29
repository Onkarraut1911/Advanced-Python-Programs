from datetime import datetime

dt = datetime.today()
print(dt)
print()

newd1 = dt.strftime("%B, %d, %Y")
print(newd1)
print()

newd1 = dt.strftime("%d/%b/%Y")
print(newd1)
print()

newd2 = dt.strftime("%d-%m-%Y")
print(newd2)
print()

newt3 = dt.strftime("%I:%M:%S")
print(newt3)
print()

newt4 = dt.strftime("%H:%M:%S")
print(newt4)
print()
