print "q1 -> door 1 or 2"

door = raw_input("> ")

if door == "1":
    print "Bear eating cake, what you do"
    print "1 take the cake"
    print "2 scream"

    bear = raw_input("> ")

    if bear == "1":
        print "yuo are dead"
    elif bear == "2":
        print "You are deadder"
    else:
        print "Clever!"

elif door == "2":
    print "You are now in heaven"
