## Multiprocessing
## CPU-bount tasks-tasks that are heavyon CPU usage. (e.g mathematical computations , data processing)
## parallel execution multipal core of CPU.

import multiprocessing  
import multiprocessing.process
import time 

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"square:{i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1)
        print(f"cube:{i*i*i}")

if __name__=="__main__":

    p1=multiprocessing.Process(target=square_number)
    p2=multiprocessing.Process(target=cube_number)

    t=time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)