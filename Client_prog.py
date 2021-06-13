import cv2
import numpy as np
import socket
import sys
import pickle
import struct

# cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostbyname(socket.gethostname())

clientsocket.connect(('192.168.2.7',8088))
data = b''
payload_size = struct.calcsize("=I")

while True:
    while len(data) < payload_size:
        packet= clientsocket.recv(4096)
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("=I", packed_msg_size)[0]
    print(msg_size)
    
    while len(data) < msg_size:
        data += clientsocket.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    frame = cv2.resize(frame, (480, 288))
    cv2.imshow('client', frame)
    if cv2.waitKey(1)== ord('q'): break

cv2.destroyAllWindows()
clientsocket.close()


'''while True:
    cap=cv2.VideoCapture(0)
    ret,frame=cap.read()
    data = pickle.dumps(frame)
    message_size = struct.pack("I", len(data))
    clientsocket.sendall(message_size + data)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()
'''
