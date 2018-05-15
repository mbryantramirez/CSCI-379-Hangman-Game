from socket import *
from sys import argv


def main():
    # Parse command line args
    if len(argv) != 3 or not argv[2].isdigit():
        print("usage: python3 client.py <server name> <server port>")
        return 1

    hostname, serverTCPPort = argv[1], int(argv[2])
    print("Client is running...")
    print("Remote host: {}, remote TCP port: {}".format(hostname, serverTCPPort))

    # Prompt user for their name
    name = input("What's your name? ")
    # Create TCP socket
    sock = socket(AF_INET, SOCK_STREAM)
    # Get IP address of server via DNS and print it(optional)
    addr = gethostbyname(hostname)
    print (addr)
    # Connect to the server program
    sock.connect((hostname, serverTCPPort))
    # Send hello message to the server over TCP connection
    message = "Hello im" + name
    sock.send(message)
    # TCP Loop
    # while True:
    # Read in from TCP port

    # Keep listening if it doesn't receive a portUDP message

    # Read the control message from the TCP socket and print its contents

    # Break from loop once needed info is received

    # Create a UDP socket

    end = False  # default end flag

    # Game loop
    while True:
        # Prompt

        valid_commands = ['start', 'end', 'guess', 'exit']

        # UDP loop
        while True:
            # Continuously Read in from UDP port

            valid_msg_types = ["instr", "stat", "end", "na", "bye"]

            # print message

            # Instruction message should be followed by stat message

            # Break once receiving info and reprompt user
        # end of UDP loop

        # If end message received, end client process
        if end:
            break
    # end of Game loop

    # Close sockets
    print("Closing TCP and UDP sockets...")


###########################################

if __name__ == "__main__":
    main()
