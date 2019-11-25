import re
import os
li= os.listdir("C:\\Users\\ssingh722\\Documents\\Python\\demo")
print(li)
for i in li:
    net = os.path.splitext(i)
    if(net[1]==".log"):
        f = open("C:\\Users\\ssingh722\\Documents\\Python\\demo\\" +i,"rb")
        data = f.read().decode()
        pattern = '\S+@\S+'

        matches = re.findall(pattern, data)
        print(matches)
        f.close()
