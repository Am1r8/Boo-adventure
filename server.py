import time
import socket
import sys
import random

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
k = False
port = 8080

new_socket.bind((host_name, port))
print( "Binding successful!\n")
print("\nThis is your IP: ", s_ip, "\n")

name = input('\nEnter name: ')

new_socket.listen(1) 


conn, add = new_socket.accept()

print("\nReceived connection from ", add[0])
print('\nConnection Established. Connected From: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected...\n\n')

conn.send(name.encode())
rand = random.randint(1,10)
print("\n\nHello, welcome to adventure op, a game where you can play with your friends on local servers.\n\n")
print("\n\n Write the first number that you think makes the game start (both of players have to choose the same number, a number between 0-10)\n\n")
print(".....")
def send():
    message = input('\nMe : ')
    conn.send(message.encode())
    lol = message
    message = conn.recv(1024)
    message = message.decode()
    print(rand, lol, message)
    print(client, ':', message)
    if message == 'exit':
        conn.close()
        sys.exit()
    elif message == 'help':
        print('\nCommands:\n\nhelp - Displays this menu\n\nexit - Exits the game\n\n')
    elif lol == str(rand) and message == str(rand):
        print('\nYou both chose the same number!\n\n')
        print("The game starts")
        print("\n\n\n\n\n**Door opens**\n\n\n\n\n")
        print("Hello billy, how you doing man, can you turn on the computer?!\n\n")
        time.sleep(0.50)
        k = True
        # conn.send(k.encode())
    


while True:
    try:
        send()
    except:
        print("there is a Problem in the script!")
        time.sleep(5)
        exit()