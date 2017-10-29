# multithreading
import threading
from queue import Queue

def process_queue():
    while True:
        current_task = task_queue.get()
        process(current_task)
        task_queue.task_done()
        # Indicate that a formerly enqueued task is complete.
        # Used by queue consumer threads

task_queue = Queue()

task_list = [TodoTask]*5

# create 5 threads, each one run the process_queue til task_done
for i in range(5):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()

start = time.time()

for current_task in task_list:
    task_queue.put(current_url)

# Blocks until all items in the queue have been gotten and processed.
task_queue.join()

print(threading.enumerate())

print("Execution time = {0:.5f}".format(time.time() - start))



# multiprocessing

#1
from multiprocessing import Pool
if __name__ == '__main__':
    start = time.time()
    with Pool(5) as p:
        print(p.map(foo, [task1_param, task2_param, task3_param]))
    print("Time taken = {0:.5f}".format(time.time() - start))

#2
from multiprocessing import Process
if __name__ == '__main__':
    p = Process(target=f, args=('param1',))
    p.start()
    p.join()

# communicate with Queue
from multiprocessing import Process, Queue
def info(q):
    q.put([42, None, 'hello'])
if __name__ == '__main__':
    q = Queue()
    p = Process(target=info, args=(q,))
    p.start()
    print q.get()    # if f put items into q
    p.join()

# communicate with Pipe
import multiprocessing as mp

def info(conn):
    conn.send(["Hello!", 1, None])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = mp.Pipe() # create pipe between p & c
    p = mp.Process(target=info, args=(child_conn,)) # info:{c put data to p}
    p.daemon = True
    p.start()
    print(parent_conn.recv())
    p.join()

    
