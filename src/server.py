from socket import *
from sys import argv
from random import *
from game import *

def main():
  # Parse command line args
  if len(argv) != 2:
    print("usage: python3 server.py <word to guess or '-r' for random word>")
    return 1

  print("Server is running...")

  # Create the TCP Socket
  print("Creating TCP socket...")

  # Bind a port to the TCP socket, letting the OS choose the port number

  # Get the port number of the socket from the OS and print it
  # The port number will be a command-line parameter to the client program


  # Configure the TCP socket (using listen) to accept a connection request

  try: # try/except to catch ctrl-c
    while True:
      # Accept the TCP Connection
      print("Waiting for a client...")


      # TCP loop
      while True:
        # Continuously Read in from TCP port


        # Keep listening if it doesn't receive a hello message


        # Extract username handling empty case



        # Create and bind a UDP socket, letting the OS choose the port number
        print("Creating UDP socket...")


        # Add a timeout to the UDP socket so that it stops listening
        # after 2 minutes of inactivity

        # Get the port number assigned by the OS and print to console


        # Put the UDP port number in a message and send it to the client using TCP
        print("Sending UDP port number to client using TCP connection...")


        # Break from loop once needed info is received

      active = False # game not active by default

      # Game (UDP) loop
      while True:
        try:
          # receive on UDP port here


        except timeout: # catch UDP timeout
          print("Ending game due to timeout...")
          break # break and wait to accept another client


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
