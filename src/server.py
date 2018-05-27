from socket import *
from sys import argv

from game import *


def main():
    # Parse command line args
    if len(argv) != 2:
        print("usage: python3 server.py <word to guess or '-r' for random word>")
        return 1

    print("Server is running...")

    # Create the TCP Socket
    print("Creating TCP socket...")
    server_sock = socket(AF_INET, SOCK_STREAM)
    # Bind a port to the TCP socket, letting the OS choose the port number
    server_sock.bind(('', 0))
    # Get the port number of the socket from the OS and print it
    port = server_sock.getsockname()[1]
    print('Server is listening on port: ' + port)
    # The port number will be a command-line parameter to the client program
    # Configure the TCP socket (using listen) to accept a connection request
    server_sock.listen(5)

    try:  # try/except to catch ctrl-c
        while True:
            # Accept the TCP Connection
            print("Waiting for a client...")
            conn, addr = server_sock.accept()
            # TCP loop
            while True:
                # Continuously Read in from TCP port
                message = conn.recv(port)
                # Keep listening if it doesn't receive a hello message
                if not data:
                    print('waiting for message')
                # Extract username handling empty case
                first, *middle, tail = message.split()
                if tail == 'im':
                    username = ''
                else:
                    username = tail
                print('A new client is connected to server!')
                print('User name:' + username)
                # Create and bind a UDP socket, letting the OS choose the port number
                print("Creating UDP socket...")
                serverSocket = socket(AF_INET, SOCK_DGRAM)
                serverSocket.bind(('', 0))
                # Add a timeout to the UDP socket so that it stops listening
                randomUDPport = serverSocket.getsockname()[1]
                print('UDP socket has port number ' + randomUDPport)
                serverSocket.settimeout(2)
                # after 2 minutes of inactivity
                # Get the port number assigned by the OS and print to console
                # Put the UDP port number in a message and send it to the client using TCP
                print("Sending UDP port number to client using TCP connection...")
                conn.send(randomUDPport)
                # Break from loop once needed info is received

        active = False  # game not active by default

        # Game (UDP) loop
        while True:
            try:
                # receive on UDP port here
                udpgamedata, udpgameaddr = serverSocket.recvfrom(1024)
            except socket.timeout:
                # catch UDP timeout
                print("Ending game due to timeout...")
                break  # break and wait to accept another client

            if
        # if ...:
        #   #Game setup
        #   active = True
        #   word, word_blanks, attempts, win = gameSetup(argv)
        #   print("Hidden Word: {}".format(word))
        #   print("Starting game...")

        #   #Send inst then stat messages

        # elif ...:

        #   word_blanks, attempts, win = checkGuess(word, word_blanks, attempts, guess, win)

        #   #Losing conditions - break if end
        #   if len(guess) > 1 and not win or attempts == 0 or win:
        #     #Handle win/lose conditions
        #     active = False
        #   else:

        # always send a response message to the client

        # end of UDP Game loop
        # close the TCP socket the client was using as well as the udp socket.

        # end of TCP loop

except KeyboardInterrupt:

# Close sockets
print("Closing TCP and UDP sockets...")

###########################################

if __name__ == "__main__":
    main()
