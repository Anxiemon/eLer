mode = input("mode? (write/read) ")
if mode == "write":
    arqwrite = open(input("file name: "), "w")
    arqwrite.write(input("text/input: "))
elif mode == "read":
    arqread = open(input("file name: "), "r")
    print("text: ", arqread.read())
else:
    exit()