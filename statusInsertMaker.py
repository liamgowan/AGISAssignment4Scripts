import random

infile = open("ids.txt","r")
line = infile.readline();
while line != "":
    val = random.randint(1,101)
    if val<=50:
        status = "H"
    else:
        status = "E"
    line = line.rstrip("\n")
    print("insert into status_table values (%s, '%s');" % (line,status))
    line = infile.readline();
infile.close()
    
