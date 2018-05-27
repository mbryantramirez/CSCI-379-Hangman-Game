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
    print(addr)
    # Connect to the server program
    sock.connect((hostname, serverTCPPort))
    # Send hello message to the server over TCP connection
    message = "Hello im" + name
    sock.send(message)
    # TCP Loop
    # while True:
    while True:
        # Read in from TCP port
        data = sock.recv(1024)
        # Keep listening if it doesn't receive a portUDP message
        if not data:
            print('Waiting for message')
        else:
            portUDPmessage = data.decode()
            # Read the control message from the TCP socket and print its contents
            print(portUDPmessage)
        # Break from loop once needed info is received
        break
    # Create a UDP socket
    udpgamesock = socket(AF_INET, SOCK_DGRAM)
    udpgamesock.bind(('', portUDPmessage))


end = False  # default end flag

# Game loop
while True:
    # Prompt
    print(" 'This is hangman. You will guess one letter at a time. If the letter is in the hidden word, the "-" will be replaced by the correct letter. Guessing multiple letters at a time will be considered as guessing the entire word (which will result in either a win or loss automatically - win if correct, loss if incorrect). You win if you either guess all of the correct letters or guess the word correctly. You lose if you run out of attempts. Attempts will be decremented in the case of an incorrect or repeated letter guess.' " )
    valid_commands = ['start', 'end', 'guess', 'exit']
    print(valid_commands)

    # UDP loop
    while True:
        # Continuously Read in from UDP port
        gamedata, addr = udpgamesock.recvfrom(1024)

        valid_msg_types = ["instr", "stat", "end", "na", "bye"]
        # print message
        print(gamedata)
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


