
from threading import Thread

def disp(a, b):
    print("Thread running", a, b)

for i in range(5):
    # t is an object of Thread class
    t = Thread(target=disp, args=(10, 20))  # Creating a thread with disp function and arguments (10, 20)     # args is Tuple
    t.start()  # Starting the thread
