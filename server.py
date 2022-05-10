"""
this is where the machine runs.
The process:
    The client sends the image by taking a picture on the app. /n
    The server makes a file for that image. /n
    The server sends the image to the machine to predict what the image is (batteries, shoes, clothes, etc)
    The machine returns the prediction
    The server sends the prediction back to the client, where the app decides what to do with the prediction(or if an error occured)
"""
from ast import For
import socket
from _thread import *
import time
import ClassModule
AData = ""
FORMAT = "utf-8"
ip = "10.0.0.251"
port = 3000
connections = 0


addr = (ip, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind(addr)
except socket.error as e:
    print(e)

sock.listen()

def HandleConnection(conn):
    print ("HandleConnection")

    """
    This is where the communication between the client and the server starts 
    each client gets their own thread(this code) when they start the app

    """

    """
    #DataArr = []
    BUFF_SIZE = 2097152
    connected = True
    Data = b""
    NData = b""
    AData = ""
    BytesRecv = 0
    """
    AData = ""
    NData = b""
    GettingAnswer = False
    TypeConn = 0
    ByteLength = 0
    DataArr = list
    try:
        ByteLength = int(conn.recv(1024).decode(FORMAT))
        print(ByteLength)

        while True:

            try: 
                #print("before conn recv")
                if len(AData) >= ByteLength:
                    print("DONEE")
                    break
                NData = conn.recv(8092)

                #print("after conn recv")
            except Exception as e:
                print(e)
            
            if not NData and not GettingAnswer:
                print(NData.decode(FORMAT))
                print("FINISHED")
                print(NData.decode(FORMAT))
                TypeConn += 1
                DataArr = AData.split('!GETNUM!')
                ByteLength = DataArr[0]
                GettingAnswer = True
                conn.close()
            else:
                """
                AData += bytes(NData).decode('utf-8')
                BytesRecv += len(NData)
                #DataArr += NData
                Data += NData
                """

                AData += NData.decode(FORMAT)
                print("recv: " + str(len(AData)))

            
            #NewData += AData
                

            #print (AData)
    except Exception as e:
        print(e)
    try:
        ReturnData = ClassModule.FindClass(AData, type="bytes")
        print(ReturnData)
        conn.sendall(ReturnData.encode(FORMAT))
        conn.close()
    except Exception as e:
        print('an error has occured') 
        print(e)
        print('^^^^^^^^^^^^^^^')
        pass         





    """
    while True:
        try:
            DataRecv = conn.recv(16777216)
            DataBuff = DataRecv

            print("STARTING DATA PROCESS")

            if not DataBuff:
                break
            else:
                ndarray
                ReturnData = ClassModule.FindClass(DataBuff, type='bytes')
                

                Data = ReturnData.encode(FORMAT)

            conn.sendall(Data)


        except Exception as e:
            print("ERROR:" + str(e))
            global connections
            connections -= 1
            conn.close()
    """

print(f"{time.time()}")

def StartDataServer():
    global connections
    print(sock.getblocking())
    print("The data server started")
    global AData
    
    while True:

        try:
            conn, addr = sock.accept()
            start_new_thread(HandleConnection, (conn,))       
            connections += 1
            print("CONNECTIONS: " + str(connections))
            #
            #conn.close()
            #print("close connection")        
        except Exception as e:
            print("ERR")
            print(e)

StartDataServer()
