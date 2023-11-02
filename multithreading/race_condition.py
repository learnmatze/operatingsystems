import threading
import time

# make additions into the global variable
def adder(amount, repeats):
    global value
    for _ in range(repeats):
        # copy the value
        tmp = value
        # suggest a context switch
        time.sleep(0)
        # change the copy
        tmp = tmp + amount
        # suggest a context switch
        time.sleep(0)
        # copy the value back
        value = tmp
 
# make subtractions from the global variable
def subtractor(amount, repeats):
    global value
    for _ in range(repeats):
        # copy the value
        tmp = value
        # suggest a context switch
        time.sleep(0)
        # change the copy
        tmp = tmp - amount
        # suggest a context switch
        time.sleep(0)
        # copy the value back
        value = tmp
 
# define the global variable
value = 0
# start a thread making additions
adder_thread = threading.Thread(target=adder, args=(1, 1000))
# start a thread making subtractions
subtractor_thread = threading.Thread(target=subtractor, args=(1, 1000))
adder_thread.start()
subtractor_thread.start()
# wait for both threads to finish
print('Waiting for threads to finish...')
adder_thread.join()
subtractor_thread.join()
# report the value
print(f'Value: {value}')