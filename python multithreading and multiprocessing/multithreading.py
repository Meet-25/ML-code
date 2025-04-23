## Multithreading
## when to use -->
### I/o-bound tasks: Task that spend mor time waiting for I/o operation(e.g , file operation , network request).
### Concurrent execution: when you want to improve the throughput of your application by performing multiple operations concurrently. 


## example without using multithreading.
import time

print("before thread useed code \n")

def print_number():
    for i in range(5):
        time.sleep(1)
        print(f"number:{i}")

def print_letter():
    for i in "abcde":
        time.sleep(1)
        print(f"letter:{i}")

t=time.time()
print_number()
print_letter()
finished_time=time.time()-t
print(finished_time)


## example by using multithreading.
import threading
import time

print("after thread using \n")


def print_number():
    for i in range(5):
        time.sleep(1)
        print(f"number:{i}")

def print_letter():
    for i in "abcde":
        time.sleep(1)
        print(f"letter:{i}")

##creating thread
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t=time.time()
##starting thread
t1.start()
t2.start()

##wait for below code execution until all above thread execution 
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)
