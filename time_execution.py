import time

def time_execution(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time