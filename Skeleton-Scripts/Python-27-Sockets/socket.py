import os
import socket
import errno

os.system('cls' if os.name == 'nt' else 'clear')

def open_socket(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        #greeting = "AAAAA"
        #s.sendall(greeting)
        data = s.recv(1024)
        print "Banner: %s" % data
        s.close()
    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            print "Connection Error: " + str(e)
        else:
            sys.exit(1)

if __name__ == "__main__":
    while True:
        answer = raw_input("Would you like to test a port: (y/n): ")
        if answer.lower() == 'n':
            break
        elif answer.lower() == 'y':
            host = raw_input("Enter host to scan: ")
            port = int(raw_input("Enter a port to scan: "))
            open_socket(host, port)
        else:
            print "The program only accpets (y/n), please try again"