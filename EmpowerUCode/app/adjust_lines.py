def adjust_lines(path):
    rf = open(path,"r")
    line = rf.read().strip()
    wf = open(path,"w")
    wf.write(line)
