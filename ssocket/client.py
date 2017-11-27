import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=80

# host=socket.gethostname()
host='www.baidu.com'
print(host)

sock.connect((host,port))
msg=sock.recv(1024)
sock.close()
print(msg)