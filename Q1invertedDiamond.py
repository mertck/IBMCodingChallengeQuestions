def diamondInverted(r):

    # width of the diamond.
    fullWidth = int(r/2)

    # length of diamond diagonally
    newSpace = fullWidth

    # stars per row.
    starRow = 1

    isPair = False

    # checks diamond size and rows
    if r % 2 == 0:
        nowPair = True
        r += 1

    for i in range(r):

        # create line.
        line = (newSpace * " ") + (starRow * "* ")

        # placement of stars
        if i < fullWidth:
            newSpace -= 1
            starRow += 1
        # placement of stars
        else:
            newSpace += 1
            starRow -= 1

        # to keep diamond shape if numbers are the same 
        if i == fullWidth and nowPair:
            continue

        # print line
        print(line)



if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        diamondInverted(r)
