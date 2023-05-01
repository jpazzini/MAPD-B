import socket
import json
import time
import random
import argparse

# Define some lists of first and last names to use for generating random messages
first_names=('John','Andy','Joe','Alice','Jill')
last_names=('Johnson','Smith','Jones', 'Millers','Darby')

# Define a function for sending messages over the socket
def send_messages(client_socket):
    try:
        while 1:
            # Generate a random message with a random name, surname, amount, delta_t, and flag
            msg = {
                'name': random.choice(first_names),
                'surname': random.choice(last_names),
                'amount': '{:.2f}'.format(random.random()*1000),
                'delta_t': '{:.2f}'.format(random.random()*10),
                'flag': random.choices([0,1], weights=[0.8, 0.2])[0]
            }
            # Encode the message as JSON and send it over the socket
            client_socket.send((json.dumps(msg)+"\n").encode('utf-8'))
            # Sleep for a short amount of time to avoid overwhelming the network
            time.sleep(0.1)

    except KeyboardInterrupt:
        # If the user presses Ctrl+C, exit gracefully
        exit()

if __name__ == "__main__":

    # Parse command-line arguments to determine the hostname to use
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname', type=str, required=True)
    args = parser.parse_args()
    print('Using hostname:', args.hostname)

    # Create a new socket and bind it to the specified hostname and port
    new_skt = socket.socket()
    host = args.hostname
    port = 5555 
    new_skt.bind((host, port))
    print("Now listening on port: %s" % str(port))

    # Wait for a client to connect to the socket
    new_skt.listen(5) #  waiting for client connection.
    c, addr = new_skt.accept()
    print("Received request from: " + str(addr))
    # connection established, send messaged
    send_messages(c)
