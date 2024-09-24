import threading

# Variables globales
want1 = False
want2 = False
b = 0
t1 = None
t2 = None


def thread_function():
    global want1, want2, b


    # Comportamiento del hilo dependiendo de si es t1 o t2
    while threading.current_thread() == t1 and want2 == False:
        want1 = True
        b += 1
        print(f"Hi, I'm the thread {threading.current_thread().name}. b = {b}")
        want1 = False
    while threading.current_thread() == t2 and want1 == False:
        want2 = True
        b += 1
        print(f"Hi, I'm the thread {threading.current_thread().name}. b = {b}")
        want2 = False


def intent3():
    global t1, t2

    # Crear e iniciar los hilos
    t1 = threading.Thread(target=thread_function, name="t1")
    t2 = threading.Thread(target=thread_function, name="t2")

    t1.start()
    t2.start()

    # Esperar a que los hilos terminen
    t1.join()
    t2.join()


if __name__ == "__main__":
    intent3()
