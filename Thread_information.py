from threading import Thread , current_thread

def disp():
    print("Child Thread Object",current_thread())

t = Thread(target=disp)
t.start()

print("Main Thread", current_thread())