def rhombusPattern(r):
    
    # prints the rohmbus like shape
    newSpace = 0
    
    # row structure
    for i in range(r):

        # sets up stars and spaces
        line = (newSpace * " ") + (r * "*")

        # fills up the left over space
        newSpace += 1

        # print line.
        print(line)



if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        rhombusPattern(r)
