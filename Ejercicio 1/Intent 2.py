import threading

want1 = False
want2 = False
b = 0
def thread():
    global want1
    global want2
    global b
    b = b+1

    while want2 == False:
        want1 = True
        b = b + 1
        print("Hi, I'm the thread {}".format(threading.current_thread().name))
        print(f"{b}")
        want1 = False
    while want1 == False:
        want2 = True
        print("Hi, I'm the thread {}".format(threading.current_thread().name))
        print(f"{b}")
        want2 = False





def intent2():

    t1 = threading.Thread(target=thread)
    t2 = threading.Thread(target=thread)
    # Wait for all threads to complete

    t1.start()

    t2.start()



    t1.join()
    t2.join()

if __name__ == "__main__":
    intent2()