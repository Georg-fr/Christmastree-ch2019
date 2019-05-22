# Lets print a christmas tree


def christmastree():
    print"Do you want to have a star on your christmas tree? yes/no"
    star = raw_input()
    if star == "yes":
        star = True
    elif star == "no":
        star = "no star"
    else:
        print "Error please use yes or no."
        christmastree()
        return
    while True:
        print"How high should the christmas tree be?"
        tree = raw_input()
        if not tree.isdigit() or int(tree)==0:
            print"Error use a positiv number."
        else:
            if star == True:
                print(" "*(int(tree)-1)+"*")
            for i in range(int(tree)):
                print (" "*(int(tree)-i-1)+"X"*(2*i+1))
            if int(tree)>=1:
                print(" "*(int(tree)-1)+"I")
            break
    raw_input("Press enter to exit")

christmastree()


