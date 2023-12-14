active = True
while active:
    mode = input("mode? (write/read/exit) \n")
    # asks what mode the user wants to use
    if mode == "write":
        arqwrite = open(input("file name: "), "w")
        arqwrite.write(input("text/input: \n"))
        arqwrite.close()
    elif mode == "read":
        arqread = open(input("file name: "), "r")
        print("text: \n", arqread.read())
        arqread.close()
    elif mode == "exit":
        active = False
    else:
        print("I think you made a typo.")
