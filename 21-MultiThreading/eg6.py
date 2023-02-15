from threading import Thread


class MyThread(Thread):

    def __init__(self, eId, eName):
        Thread.__init__(self)
        self.eId = eId
        self.eName = eName

    def run(self):
        print(self.eId, self.eName)


t = MyThread(101, "NameOne")
t.start()

t = MyThread(102, "NameTwo")
t.start()
