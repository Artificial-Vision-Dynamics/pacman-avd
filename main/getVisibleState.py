def getVisibleState:
    # Returns the content of the adjacent squares

    # Config parameters
    shape = 'cross'
    widthRange = 3
    heightRange = 3

    # Building the observable area
    pos = s.getPacmanPosition()
    if shape == 'cross':
        listX = range(pos(1) - widthRange, pos(1) - 1)
        listX.append(range(pos(1) + , pos(1) + widthRange))
        listY = range(pos(2) - heightRange, pos(2)- 1)
        listY.append(range(pos(2) + 1, pos(2) + heightRange))
        obsArea = [];

        y = pos(2)
        for x in listX:
            obsArea.append([x, y])
        x = pos(1)
        for y in listY:
            obsArea.append([x, y])

    # Getting info from the state
    currentFood = self.getFood()
    walls = self.getWalls()
    ghosts = self.getGhostsPositions()
    
    # Observable state
    i = 1
    for square in obsArea:
        if square == pos:
            continue
        #elif # Fin del mapa
        elif currentFood(square) == True:
            obsState[i] = 'f'
        elif walls(square) == True:
            obsState[i] = 'w'
        else:
            obsState[i] = ''
            for ghostPos in ghosts:
                if ghostPos == square:
                    obsState[i] = 'g'
        
        i += 1            