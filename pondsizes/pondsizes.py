def getPondSizes(waterSquares):
    ponds = []
    unexploredWater = set(waterSquares)

    while len(unexploredWater) > 0:
        waterPosition = unexploredWater.pop()

        ponds.append(countAdjacentWater(waterPosition, unexploredWater))
    return ponds

def countAdjacentWater(position, unexploredWater):
    xPos = position[0]
    yPos = position[1]

    waterCount = 1

    adjacentSquares = [
        (xPos + 1, yPos),
        (xPos - 1, yPos),
        (xPos, yPos + 1),
        (xPos, yPos - 1),
        (xPos - 1, yPos - 1),
        (xPos + 1, yPos - 1),
        (xPos - 1, yPos + 1),
        (xPos + 1, yPos + 1)
    ]

    for square in adjacentSquares:
        if square in unexploredWater:
            unexploredWater.remove(square)
            waterCount += countAdjacentWater(square, unexploredWater)

    return waterCount
