from threading import Thread, current_thread
import time
def disp1():
    print("Default Child Thread Name : ", current_thread().name)
    # current_thread().setName('Doc Thread')
    current_thread().name = 'Doc Thread'
    print("New Child Thread Name : ",current_thread().name)

def disp():
    print("Default Child Thread Name : ", current_thread().name)
    # current_thread().setName('Doc Thread')
    current_thread().name = 'Doc Thread'
    print("New Child Thread Name : ",current_thread().name)
    

t = Thread(target=disp)
t2 = Thread(target=disp)
t3 = Thread(target=disp , name = 'raj thread')    # you can direcly right this
print(t3)
t.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()
time.sleep(1)

time.sleep(1)
print("Main Thread Name : ", current_thread().name)
# current_thread().setName('Show Thread')              
current_thread().name = 'Show Thread'                    
print("New Main Thread Name : ", current_thread().name)

# This code uses the name attribute directly rather than setName() method to set the name for the threads, thus avoiding the DeprecationWarning.
