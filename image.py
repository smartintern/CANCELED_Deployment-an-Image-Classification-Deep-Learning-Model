#!/usr/bin/env python3
import os, sys, socket

# open a file
path = "/home/emine/picture/train/"
dirs = os.listdir(path)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 1000))
s.listen(10) # 10 clients can be connected

# Gelen dosyaların hepsi 'dosya' isminde kaydedileceği için dosya isimlerine numara ekleyelim. 
count = 0
for i in os.listdir(os.getcwd()):
    if i.startswith("dosya"):
        count +=1

file_no = count

print("Server is up... Clients are expected...")

while True:
    c, addr = s.accept()
    print('\n{} connected'.format(addr))
    datas = c.recv(1024)
    f = open("dosya{}.png".format(file_no), "wb")
    while datas:
        f.write(datas)
        datas = c.recv(1024)
    f.close()

    print("File received...".format(file_no))
    file_no += 1
    continue
















