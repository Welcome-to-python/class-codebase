from datetime import datetime

text = input()

file = open("log.txt", "a")

file.write(str(datetime.now()) + " : " + text + "\n")

file.close()