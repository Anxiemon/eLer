active = True
while active:
    mode = input("mode? (write/read/exit) \n")
    if mode == "write":
        arqwrite = open(input("file name: "), "w")
        arqwrite.write(input("text/input: \n"))
    elif mode == "read":
        arqread = open(input("file name: "), "r")
        print("text: \n", arqread.read())
    elif mode == "exit":
        active = False
    else:
        print("I think you made a typo.")
