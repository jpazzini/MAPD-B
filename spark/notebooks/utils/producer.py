import socket
import json
import time
import random
import argparse

first_names=('John','Andy','Joe','Alice')
last_names=('Johnson','Smith','Jones', 'Millers')

def send_messages(client_socket):
    try:
        while 1:
            msg = {
                'name': random.choice(first_names),
                'surname': random.choice(last_names),
                'amount': '{:.2f}'.format(random.random()*1000),
                'delta_t': '{:.2f}'.format(random.random()*10),
                'flag': random.choices([0,1], weights=[0.8, 0.2])[0]
            }
            client_socket.send((json.dumps(msg)+"\n").encode('utf-8'))
            time.sleep(0.1)

    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname', type=str, required=True)
    args = parser.parse_args()
    print('Using hostname:', args.hostname)

    new_skt = socket.socket()
    host = args.hostname
    port = 5555 
    new_skt.bind((host, port))
    print("Now listening on port: %s" % str(port))

    new_skt.listen(5) #  waiting for client connection.
    c, addr = new_skt.accept()
    print("Received request from: " + str(addr))
    # connection established, send messaged
    send_messages(c)
    
