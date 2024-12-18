from multiprocessing import Process 
import time 


def print_alphabets():
    string = "Hello Welcome"
    for char in string:
        time.sleep(1)
        print(char)

def print_numbers():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    for num in numbers:
        time.sleep(1)
        print(num)

if __name__ == "__main__":
    start_time = time.time()
    t1 = Process(target=print_alphabets)
    t2 = Process(target=print_numbers)

    t1.start()
    t2.start()

    t1.join()
    t2.join() 
    end_time = time.time() - start_time 
    print("finished time", end_time)
    