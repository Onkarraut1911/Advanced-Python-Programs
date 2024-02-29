from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread")

t = Mythread()
t.start()
t.join()  # join function running thread one by one , now first run child thread after run main thread
for i in range(5):
    print("Main Thread")
