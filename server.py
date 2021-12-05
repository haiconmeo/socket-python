# first of all import the socket library
import socket			


s = socket.socket()		
print ("Socket successfully created")

port = 9001			


s.bind(('', port))		
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)	
print ("socket is listening")		

# a forever loop until we interrupt it or
# an error occurs
while True:

# Establish connection with client.
    connect, addr = s.accept()	
    print ('Got connection from', addr )

    # send a thank you message to the client. encoding to send byte type.
    connect.send('Thank you for connecting'.encode())
    data = connect.recv(1024)
    print (data, 'EOF')

    # Close the connection with the client
    connect.close()

# Breaking once connection closed
    break
