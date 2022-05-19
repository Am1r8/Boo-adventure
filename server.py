import time
import socket
import sys
import random
from time import sleep
import os

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
sleep(1)
print("\n\n Write the first number that you think makes the game start (a number between 0-10)\n\n")
sleep(1)
print(".....")
sleep(5)
os.system('cls')
r = 0
def send():
    # message = input('\nMe : ')
    # conn.send(message.encode())
    # lol = message
    message = conn.recv(1024)
    message = message.decode()
    print(rand, message)
    print(client, ':', message)
    if message == 'exit':
        conn.close()
        sys.exit()
    elif message == 'help':
        print('\nCommands:\n\nhelp - Displays this menu\n\nexit - Exits the game\n\n')
    elif message == str(rand):
        print('\nYou both chose the same number!\n\n')
        print("The game starts")
        print("\n\n\n\n\n**Door opens**\n\n\n\n\n")
        print("Hello billy, how you doing man, can you turn on the computer?!\n\n")
        time.sleep(0.50)
        print("\n\nWhat was the password?")
        print("it was my birthday year I am 19 years old!")
    elif message == str(2022-19):
        print("\nI am in\n")
        print("What should I do now?\n\njack where did you go\n\n(He is probably in the kitchen)")
        print("\n\ndid you cut your hand? there is blood in the sink! What should I do?!\n 11) call 911\n 12) clean the blood it's probally from last nights cake\n 13) Scream Jack")
    elif message == str(11):
        print("**RING RING**\nWhy they are not picking up?!\nLet me call again\n**RING RING**\nNo answer what should I do?!\n\n should I clean the blood with a rag? (Y/N)\n\n")
    elif message == "Y":
        print("I Should clean this off and go home I don't want to deal with this guy jokes!\n\n")
        exit()
    elif message == "N":
        print("I should call his mom or someone!\nI am calling his mom\n\n**RING RING RING** ......\n Hello miss I was with jack and he is missing what should I do, there is blood in the sink too, I am not sure if its his.\nMam can you hear me?! .........\n\n what's going on with this family?! **LIGHTS GO OUT**\n\n^%^!#(!(**((@&*!#\nJack dude this is not funny I am leaving\n")
        print("Why the door is locked!!!!!!!!!!\n\nNo batteries on my phone too I can't use the flash\n What should I do?\n 14) Break the glass and run\n 15) Stay and figure out what's going on?")
    elif message == "14":
        print("\nWhat was that sound I should hurry up and get out of here!\nThe sound is getting closer wtf is going on?!\ndude I should get out!\n\nWhat should I use to brake the window?\nknife\nchair\ndog")
    elif message == "knife":
        print("I can't use this choose another option!\n\nWhat should I use to brake the window?\nchair\ndog")
    elif message == "chair":
        print("**PAGH PAGH** The windows is broken, runnnnnnnnnnnnnnnn")
        print("\nYou Won\n")
        exit()
    elif message == "dog":
        print("**Bark Bark Bark** I can't use her, she is gonna die!\nYou are too brutal you lost")
        exit()
    elif message == "15":
        print("Jack where are you dude?!\nThis is not funny at all. (what was that sound, it was from basement) **PAGH** **TURNS ON THE LIGHT**\nYou here? I'm gonna kill you if I find you! **GASP** what is that?!!!!!!!!!!!!!!\n\n(RUN RUN)\nbreak the window with a chair and run!")
        print("Press 'r' as much as you can!")
    elif message == "r":
        r += 1
        if r == 10:
            print("YOU ARE SAFE, YOU WON!")
            sleep(7)
            exit()

while True:
    try:
        send()
    except:
        print("there is a Problem in the script!")
        time.sleep(5)
        exit()