from threading import Thread, current_thread

def disp():
    # print("Child Thread Name : ", current_thread().getName())
    print("Child Thread Name : ", current_thread().name)

t = Thread(target=disp)
t2 = Thread(target=disp)
t.start()
print()
t2.start()

print()
# print("Main Thread Name : ", current_thread().getName())
print("Main Thread Name : ", current_thread().name)



# By using current_thread().name instead of current_thread().getName(), you can avoid the DeprecationWarning.