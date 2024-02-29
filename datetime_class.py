from datetime import datetime
dt = datetime(year=2024, month=2, day=28)
dt2 = datetime(year=2023,month=4,day=1,hour=22,minute=50)
dt3 = datetime(2017, 4 ,28)
dt4 = datetime(2016 , 3 ,17 , 14 , 30)

print(dt)
print(dt2)
print(dt3)
print(dt4)
print()

print(dt.day,end="/")
print(dt.month,end="/")
print(dt.year)