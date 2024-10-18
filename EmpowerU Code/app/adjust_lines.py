def adjust_lines(path):
    rf = open(path,"r")
    line = rf.readline()
    condition = False
    if line[-1] == "\n":
        condition = True
    if condition == True:
        wf = open(path,"w")
        wf.write(line[0:-1])