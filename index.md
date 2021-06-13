# Summer Program Task 3

📌 Created Live Streaming Video Chat App without voice using cv2 module of Python: 

Successfully completed the video streaming app without voice using python.

### Libraries used- 
#### 1. opven cv:
Download this library using $pip install opencv-python
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.
		
This library helped in reading (capturing) and displaying the data send over the network. 

#### 2. Socket:
Socket programming is used to connect 2 nodes on a network to establish communication between them. At a particular time, One socket(node) listens on a port, usually a Server socket, while other socket reaches out to form a connection,  usually a client. 

Socket programming is used whenever a server client architecture is needed.

Here we imported socket library and passed two parameters, AF_INET which refers to address family of ipv4 and SOCK_STREAM  which signifies TCP oriented protocol.

#### 3. Pickel:
The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”;

We used pickle.dump() and pickle.load() to pass and retrieve data.

Using all these libraries, Video streaming program was created successfully!

![demo img](/img1.png)
