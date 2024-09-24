import threading

turn = 1
def thread():
    print("Hi, I'm the thread {}".format(threading.current_thread().name))

def intent1():
    global turn
    t1 = threading.Thread(target=thread)
    t2 = threading.Thread(target=thread)
    while True:
        while (turn == 0):
            t1.start() # start the thread
            turn = 1

        while (turn == 1):
            t2.start()
            turn = 0

    # Wait for all threads to complete
    t1.join()
    t2.join()

    print("End")

if __name__ == "__main__":
    intent1()
