f=open("download.jpg","rb")
chunk=2048
i=1
while True:
    data=f.read(chunk)
    if not data:
        break
    fo=open("chunk"+str(i)+'.jpg','wb')
    fo.write(data)
    fo.close()

