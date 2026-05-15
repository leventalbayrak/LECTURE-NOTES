
file = open("mydiary.txt", "r")
text = file.read()
file.close()

#secret message characters from 23 to 39 in reverse
msg = text[39:22:-1]

file = open("secretmessage.txt", "w")
file.write("your secret message is:\n")
file.write(msg)
file.write('\n')
file.write("\n******\ngoodbye!")
file.close()