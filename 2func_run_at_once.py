from threading import Thread

def fun1():
    for i in range(3):
        print("Working1")
def fun2():
    for i in range(4):
        print("Working2")

t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t1.start()
t2.start()