def flipAndInvertImage(image):

    flipped_image = []
    coords = []
    n = len(image[0]) - 1

    for i in range(len(image)):
        for j in range(n, -1, -1):

            if image[i][j] == 0:
                coords.append(1)
            elif image[i][j] == 1:
                coords.append(0)

            
        flipped_image.insert(i, coords)
        coords = []

    return flipped_image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
flipAndInvertImage(image)
