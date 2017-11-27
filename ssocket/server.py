import socket,sys

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

hostName=socket.gethostname()

port=9999

serverSocket.bind((hostName,port))
no=1
serverSocket.listen(5)
while True:
    clientSocket,addr=serverSocket.accept()
    print("连接地址:",addr)
    msg='your client no:'+str(no)
    no+=1
    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()