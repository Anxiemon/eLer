mode = input("mode? (write/read) \n")
if mode == "write":
    arqwrite = open(input("file name: "), "w")
    arqwrite.write(input("text/input: \n"))
elif mode == "read":
    arqread = open(input("file name: "), "r")
    print("text: \n", arqread.read())
    input("\n Press Enter to exit")
else:
    exit()
