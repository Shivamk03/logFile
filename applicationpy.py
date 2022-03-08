from fileinput import close


f=open("test.txt","r")
lines=f.readlines()
for line in lines:
    line=line.split(' ')
    print(line[0])
f.close()
with open ("test.txt","a") as a:
    a.write("vipul")
