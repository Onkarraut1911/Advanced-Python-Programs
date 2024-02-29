from datetime import timedelta , date
td = timedelta(days=10)
d = date.today()
print("After 10 days from today",d+td)
print("Befor 10 days from today",d-td)