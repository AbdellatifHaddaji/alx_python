for i in range(10):
    for j in range(i + 1, 10):
        print("{:02d}".format(int(str(i) + str(j))), end=", " if (i, j) != (8, 9) else "\n")