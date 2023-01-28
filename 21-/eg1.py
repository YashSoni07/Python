import threading

t = threading.current_thread().name
print(t)

t = threading.main_thread().name
print(t)

if threading.current_thread() == threading.main_thread():
    print("Main Method Executed")
else:
    print("Some Other Method")
