### advanced multi-threading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"number:{number}"

numbers=[1,2,3,4,5]


with ThreadPoolExecutor(max_workers=4) as executor:
    results=executor.map(print_number,numbers)

for i in results:
    print(i)
