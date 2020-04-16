command = input("> ")
started = False
while command.upper() != "QUIT":
    command = command.upper()
    if command == "HELP":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
        print("")
        command = input("> ")
    elif command == "START":
        if started:
            print("Car is already started!")
            print("")
            command = input("> ")
        else:
            started = True
            print("Car started...Ready to go!")
            print("")
            command = input("> ")

    elif command == "STOP":
        if not started:

            print("Car is already stopped!")
            print("")
            command = input("> ")

        else:
            started = False
            print("Car stopped.")
            print("")
            command = input("> ")

    else:
        print("I don't understand that...")
        print("")
        command = input("> ")
