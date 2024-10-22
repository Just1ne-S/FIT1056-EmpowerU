def adjust_lines(path):
    with open(path, "r") as rf:
        line = rf.read().strip()
    with open(path, "w") as wf:
        wf.write(line)
