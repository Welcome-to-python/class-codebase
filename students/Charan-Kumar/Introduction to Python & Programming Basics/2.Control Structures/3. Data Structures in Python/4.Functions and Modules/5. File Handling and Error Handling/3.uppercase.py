try:
    infile = open("input.txt", "r")
    outfile = open("output.txt", "w")

    for line in infile:
        outfile.write(line.upper())

    infile.close()
    outfile.close()

    print("Contents copied in uppercase to output.txt")

except FileNotFoundError:
    print("Input file not found!")