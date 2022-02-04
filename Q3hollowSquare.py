def hollowSquarePattern(r):
    
    # sets up the range and keeping the square hollow
    hollowMiddle = r - 2

    # row structure
    for i in range(r):

        # prints the parts with the stars
        if i == 0 or i == r - 1:
            line = "*" * r
        # sets up the hollow parts
        else:
            line = "*" + (hollowMiddle * " ") + "*"

        # print  line.
        print(line)



if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        hollowSquarePattern(r)
