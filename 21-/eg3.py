import threading

if __name__ == "__main__":
    pass

t1 = threading.current_thread()
t2 = threading.main_thread()

if t1 == t2:
    print("True")
    print(t1.ident)
    print(t2.ident)
else:
    print("False")
    