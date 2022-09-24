import threading
import socket
if __name__ == '__main__':
    def rcv(sok:socket.socket):
        while not sok._closed:
            print(sok.recv(256).decode('utf-8'))
    def rc(i):
        s = socket.socket()
        s.connect(('39.103.202.86', 12000))
        r = s.recv(256)
        s.sendall(str(i + 2000).encode('utf-8'))
        threading.Thread(target=rcv, args=(s,)).start()
        while i != 'close':
            s.sendall((i:=input()).encode('utf-8'))
        s.close()

    # for i in range(3):
    #     t = threading.Thread(target=rc, args=(i,))
    #     print('start', i)
    #     t.start()
    #     t.join()
    for i in range(5):
        threading.Thread(target=rc, args=(i,)).start()
