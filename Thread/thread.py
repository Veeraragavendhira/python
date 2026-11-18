import threading
def display():
    print("Hello Thread")
def deepak():
    print("deepak function")
t = threading.Thread(target=display)
a = threading.Thread(target=deepak)
t.start()
a.start()
