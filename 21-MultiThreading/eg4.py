from threading import Thread


def displayNumber():
    i = 0
    while i <= 10:
        print(i)
        i += 1


t = Thread(target=displayNumber())
print(t)
