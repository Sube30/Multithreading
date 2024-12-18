from concurrent.futures import ThreadPoolExecutor
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
    with ThreadPoolExecutor(max_workers=5) as executor:
        
        results = executor.submit(print_alphabets)

        results1 = executor.submit(print_numbers)
        results.result() 
        results1.result()

    end_time = time.time() - start_time 
    print("finished time", end_time)