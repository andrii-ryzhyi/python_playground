from threading import Thread
import time

is_wait = True
is_daemon = True

def thread_launcher(thread_name, is_daemon=False):
    def inner(fn):    
        def wrapper(is_wait, *args, **kwargs):
            t = Thread(target=fn, args=(is_wait,), name=thread_name)
            t.daemon = is_daemon
            print(f"Thread name: {t.getName()}")
            t.start()
            if is_wait: 
                t.join()
        return wrapper
    return inner

@thread_launcher("Thread name", is_daemon)
def some_func(is_wait):
    print("Some work execution...")
    time.sleep(3)
    print("Work done")

some_func(is_wait)

