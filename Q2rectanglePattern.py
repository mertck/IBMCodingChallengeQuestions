def rectanglePattern(w, h):

    # creation of rows
    for i in range(h):
        # prints row and width
        print(w * "*")
    


if __name__ == "__main__":

    h = int(input("Enter the number of rows : "))
    w = int(input("Enter the number of cols : "))

    if h != None and w != None:
        rectanglePattern(w, h)
