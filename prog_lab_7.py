import random
import string
import threading
import time

strings=[]

class Potok1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon=True


    def run(self):
        while True:
            strings.append(self.generate_random_string())

    def generate_random_string(self):
        length = 10
        letters = string.ascii_letters
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

class Potok2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.deamon=True

    def run(self):
        while True:
            print(strings)

class Potok3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.deamon=True

    def run(self):
        while True:
            strings.sort()
            time.sleep(5)
t1=Potok1()
t2=Potok2()
t3=Potok3()

t1.start()
t2.start()
t3.start()