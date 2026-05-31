with open("input.txt") as f, open("output.txt","w") as out:
    for line in f:
        out.write(line.upper())
