lastWinnerScore = 0

def bestPath(paths, targetPos, cicle, bestPath, log):
    '''calculating what path was the closest to the target'''
    global lastWinnerScore

    pathCopy = {}

    if (log) : print('target position is ', targetPos.x, targetPos.y)
    print('\n')
    for i in paths:
        currPath = paths[i]
        #distance from the target'
        distance = int(currPath[ len( currPath ) -1 ].nonRootedDistance(targetPos))

        #pushing the distance in an array allongside the name
        pathCopy[i] = distance

        if (log) : print('current path', currPath[len(currPath)-1].x, currPath[ len( currPath ) -1 ].y , i)
            
        if (log) : print('path distance', distance, '\n')

    #for the guy who won the race!
    winner = sorted(pathCopy, key = pathCopy.__getitem__ )[0]
    winnerScore = pathCopy[winner]
    #the path the winner traveled
    theBestPath = paths[ winner ]

    if (log) : print('and the best path is : ' )

    #for i in theBestPath :
        #if (log) : print('x:', i.x, 'y:', i.y)
    
    if (log) : print('\n')
    if (log) : print('and the winner is is ::: ', winner )
    if (log) : print(winner, " 's winner distance is ::: ", winnerScore )
    
    if (winnerScore > lastWinnerScore) :
        if (log) : print('congrats ', winner , ' !!!')
        return winner
    else : 
        return 0 
        print (' to bad, the last score was better :( ')

    lastWinnerScore = winnerScore
    if (log) : print('this was cycle : ', cicle)
    #returnint the best path
