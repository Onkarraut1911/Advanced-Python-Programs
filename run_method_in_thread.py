from threading import Thread

class Mythread(Thread):    # This is Mythread class inherited from Thread class in the threading module
    def run(self):          # run method defined in Thread class in this class is override run method    
        print("Run Method")

t = Mythread()
print(t.name)
print()
t.start()   # only when run method called if we run the start() function because run method run after the start method 