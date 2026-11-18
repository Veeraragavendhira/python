import threading
def task1():
    a = 0
    while(a<=100):
        print(a)
        a+=10
def task2():
    print("Task 2 Running")
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t1.join()
t2.start()
t2.join()
print("Completed")
