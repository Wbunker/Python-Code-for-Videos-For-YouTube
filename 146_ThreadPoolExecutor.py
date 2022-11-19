import requests
import time
from concurrent.futures import ProcessPoolExecutor


work = range(500000, 500200)

def cpu_task(n):
    return sum(i * i for i in range(n))

if __name__=='__main__':
    # start_time = time.time()
    # for x in work:
    #     cpu_task(x)

    # serial_time = time.time() - start_time
    # print(f"Serial time: {serial_time}")  

    with ProcessPoolExecutor(max_workers=8) as pool:
        start_time = time.time()
        for result in pool.map(cpu_task, work):
            pass
        parallel_time = time.time() - start_time
    print(f"Parallel time: {parallel_time}")