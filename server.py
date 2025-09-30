import socket
from _thread import *
from Player import player
import pickle
import os

dir = os.getcwd()

server = "192.168.1.103"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


players = [player(0,0,80,80,2,f"{dir}\\Sample Project #1\\images\\player.png"), player(100,100, 80,80,2,f"{dir}\\Sample Project #1\\images\\playerR.png")]

def threaded_client(conn, player):
    if player > 1:
        player = 1
    print(player)
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 0:
                    reply = players[0]
                    #print(f"player 1 {player}")
                else:
                    reply = players[1]
                    #print(f"player 2 {player}")

                #print("Received: ", data)
                #print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = -1
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    print(currentPlayer)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1