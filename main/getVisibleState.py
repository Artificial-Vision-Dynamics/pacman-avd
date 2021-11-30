def getVisibleState:
    # Returns the content of the adjacent squares

    # Config parameters
    shape = 'cross'
    width = 8
    height = 8

    # Building the observable area
    pos = s.getPacmanPosition()
    listX = range(pos(1) - width/2, pos(1) - 1)
    listX.append(range(pos(1) + , pos(1) + width/2))
    listY = range(pos(2) - height/2, pos(2)- 1)
    listY.append(range(pos(2) + 1, pos(2) + height/2))
    obsArea = [];
    if shape == 'cross':
        y = pos(2)
        for x in listX:
            obsArea.append([x, y])
        x = pos(1)
        for y in listY:
            obsArea.append([x, y])

    # Getting info from the state
    currentFood = state.getFood()
    walls = state.getWalls()
    ghosts = state.getGhostsPositions()
    
    # Observable state
    for square in obsArea:
        if currentFood(square) == True:
            obsState(square) = 'f'
        elif walls(square) == True:
            obsState(square) = 'w'
        elif 
            