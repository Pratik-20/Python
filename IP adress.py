import socket as s
hn = s.gethostname()
IPAD = s.gethostbyname(hn)
print("IP adress is" + IPAD)
#