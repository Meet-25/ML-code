### multiprocessing  

from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"number:{number}"

numbers=[1,2,3,4,5,6,7,8,9]

if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        results=executor.map(print_number,numbers)

    for i in results:
        print(i) 
