for i in range(2, 101):
    for o in range(2, 101):
        # If this number divides the other number, print it to the screen
        if(i % o == 0):
            print("{} divides {}".format(o, i))