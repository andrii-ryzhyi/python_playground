from threading import Thread
import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

is_wait = True
is_daemon = True

urls = []
urls.append('https://google.com')
urls.append('https://udacity.com')
urls.append('https://hotline.ua')
urls.append('https://olx.ua')
urls.append('https://pluralsight.com')
urls.append('https://yahoo.com')
urls.append('https://linuxacademy.com')
urls.append('https://youtube.com')
urls.append('https://wikipedia.com')
urls.append('https://facebook.com')

def thread_launcher(urls):
    def inner(fn):    
        def wrapper(*args, **kwargs):
            threads = []

            print("Creating threads ...")
            for i in range(len(urls)):
                thread = Thread(target=fn, args=(urls[i],), name=f"Thread {i}")
                threads.append(thread)

            print("Starting threads execution")
            for thread in threads:
                print(f"{thread.getName()}")
                thread.start()
                #thread.join()
            
        return wrapper
    return inner

@thread_launcher(urls)
def get_url(url):
    print(f"Starting url {url}")
    try:
        response = requests.get(url, verify=False)        
    except requests.exceptions.RequestException as err:
        return err
    print(f"{url}  ->  success")
    return response

get_url(urls)


