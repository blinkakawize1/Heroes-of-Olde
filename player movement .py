def main():
    Player = dict(x=0, y=0, gfc='@')#character has an x, y, and a char graphic
    Cell = dict()#for every x on the map, a cell is generated with an x and y coordinate
    CellList = []#cells are stored in a list
    
    DemoMap = {'map': '''
ooooooooooo
ox.xxxxxxxo
oxxx,xx.xxo
oxxxxxxxxxo
oxxx,xxxxxo
ox,xxxxx.xo
ooooooooooo''', 'w': 11, 'h': 7}#the map is 11x7.. width and height are used to measure it.
                                #the edges of each map are lined with o's to indicate the edge of the map.
                                #maps have all kinds of graphics in them, and graphics represent different things
                                #like nature, objects, people, or buildings
    def initialize_map():
        DemoMap['map'] = DemoMap['map'].replace('\n', '')#all new lines are deleted from the maps
        DemoMap['map'] = DemoMap['map'].replace('x', ' ')#x's are replaced with spaces to make the map feel open
        
        wCounter = 1#the width and height counter are used so the function prints
        hCounter = 1#according to the dimension of the map
        for e in DemoMap['map']:
            Cell[e] = dict(x=wCounter, y=hCounter, gfc=f'{e}')#cells are given an x,y and graphic
            CellList.append(Cell[e])
            print(Cell[e]['gfc'], end='')
            wCounter += 1
            if wCounter > DemoMap['w']:
                wCounter = 1
                hCounter += 1
                print()

    def refresh_map():#every time the user inputs a move, the map is refreshed
        wCounter = 1
        for cell in CellList:
            if cell['x'] == Player['x'] and cell['y'] == Player['y']:#this condition assigns a graphic to the temporary
                tempGfc = Player['gfc']                              #variable which tells the function what graphic to print
            else:
                tempGfc = cell['gfc']
            print(tempGfc, end='')
            wCounter += 1
            if wCounter > DemoMap['w']:
                wCounter = 1
                print()
        
    def move_player():
        while True:
            playerDirection = input("Which way? ")#input is used and takes w,s,a, or d to move in 4 directions.
            if playerDirection == 'a':
                if Player['x'] == 1:#if the user is at the edge of the map, it doesns't move the player coordinate.
                    print('out of bounds')
                    continue
                Player['x'] -= 1
            
            elif playerDirection == 'd':
                if Player['x'] == DemoMap['w']:
                    print('out of bounds')
                    continue
                Player['x'] += 1
            
            elif playerDirection == 'w':
                if Player['y'] == 1:
                    print('out of bounds')
                    continue
                Player['y'] -= 1
            
            elif playerDirection == 's':
                if Player['y'] == DemoMap['h']:
                    print('out of bounds')
                    continue
                Player['y'] += 1
            refresh_map()

                
    def spawn_player():#this is used for when the user loads a new map
        while True:
            spawnBoolean = input("Spawn player?")
            if spawnBoolean == 'y':
                Player['x'] = 6
                Player['y'] = 4
                refresh_map()
                break
            else:
                continue
                
    initialize_map()
    spawn_player()
    move_player()

main()
