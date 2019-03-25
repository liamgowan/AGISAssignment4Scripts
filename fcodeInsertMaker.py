infile = open("fcodeToInserts.txt","r")
line = infile.readline();
while line != "":
    line = line.rstrip("\n")
    lineSplit=line.split(":")
    print("insert into fcode_lut values ('%s', '%s');" % (lineSplit[0],lineSplit[1]))
    line = infile.readline();
infile.close()
    
