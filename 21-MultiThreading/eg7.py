import threading
from threading import Thread
import time


class MyThread(Thread):

    def run(self):
        for i in range(5):
            time.sleep(2)
            print(i, "Child Thread")


t1 = MyThread()
t1.start()
t1.join()

t2 = MyThread()
t2.start()
t2.join()