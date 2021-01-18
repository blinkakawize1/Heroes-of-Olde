import tkinter as tk

def main():

    Root = tk.Tk()
    Root.title("Olde Game Engine")
    Root.geometry('1366x768')

    LeftP = tk.Frame(Root, bg='dark green', borderwidth='1', relief='raised')
    LeftP.pack(side='left', fill='both', expand='false')

    CenterP = tk.Frame(Root, bg='dark green', borderwidth='1', relief='raised')
    CenterP.pack(side='left', fill='both', expand='false')

    RightP = tk.Frame(Root, bg='dark green', borderwidth='1', relief='raised')
    RightP.pack(side='left', fill='both', expand='true')

    StatW = tk.Frame(RightP, bg='gray', borderwidth='1', relief='groove')
    StatW.pack(fill='x', expand='false')

    StatL = tk.Label(StatW, text='StatW', bg='green')
    StatL.pack(fill='both', expand='true')

    HealthL = tk.Label(StatW, text='Health: 100', bg='red')
    HealthL.pack(fill='both', expand='true')

    ManaL = tk.Label(StatW, text='Mana: 100', bg='blue')
    ManaL.pack(fill='both', expand='true')

    EnergyL = tk.Label(StatW, text='Energy: 100', bg='green')
    EnergyL.pack(fill='both', expand='true')

    FatigueL = tk.Label(StatW, text='Fatigue: 100', bg='brown')
    FatigueL.pack(fill='both', expand='true')

    MenuW = tk.Frame(RightP, bg='gray', borderwidth='1', relief='groove')
    MenuW.pack(fill='x', expand='false')

    MenuL = tk.Label(MenuW, text='MenuW', bg='green')
    MenuL.pack(fill='both', expand='true')

    CharacterW = tk.Text(RightP, bg='black', fg='white', width=25, height=34)
    CharacterW.pack(fill='x')

    NavW = tk.Frame(LeftP, bg='gray', borderwidth='1', relief='groove')
    NavW.pack()

    NavL = tk.Label(NavW, text='NavW', bg='green')
    NavL.pack(fill='both', expand='true')

    TimeL = tk.Label(NavW, text='Time: Solus Era: 1st hour', bg='yellow')
    TimeL.pack(fill='both', expand='true')

    LocL = tk.Label(NavW, text='Location: The place with a really long name.', bg='magenta')
    LocL.pack(fill='both', expand='true')

    TarL = tk.Label(NavW, text='Target: A very interesting person!', bg='orange')
    TarL.pack(fill='both', expand='true')

    EventL = tk.Label(LeftP, text='EventW', bg='green')
    EventL.pack(fill='both')

    EventW = tk.Text(LeftP, bg='light blue', width=37, height=22)
    EventW.pack()

    ChatL = tk.Label(LeftP, text='ChatW', bg='green')
    ChatL.pack(fill='both')

    ChatW = tk.Text(LeftP, bg='light blue', width=37)
    ChatW.pack(fill='y')

    SceneL = tk.Label(CenterP, text='SceneW', bg='green')
    SceneL.pack(fill='both')

    SceneW = tk.Text(CenterP, width=90)
    SceneW.pack(side='left', fill='both')
    
    Player = dict(x=0, y=0, gfc='@')#character has an x, y, and a char graphic
    Cell = dict()#for every x on the map, a cell is generated with an x and y coordinate
    CellList = []#cells are stored in a list

    DemoMap = {'map': '''
........................................
........................................
........................................
........................................
........................................
........................................
........................................''', 'w': 40, 'h': 7}#the map is 40x7.. width and height are used to measure it.
                                #the edges of each map are lined with o's to indicate the edge of the map.
                                #maps have all kinds of graphics in them, and graphics represent different things
                                #like nature, objects, people, or buildings

    rootActive = True
    while rootActive:
        Root.update()
        if not rootActive:
            Root.quit()
        else:
            def initialize_map():
                Root.update()
                DemoMap['map'] = DemoMap['map'].replace('\n', '')#all new lines are deleted from the maps
                DemoMap['map'] = DemoMap['map'].replace('x', ' ')#x's are replaced with spaces to make the map feel open
                
                wCounter = 1#the width and height counter are used so the function prints
                hCounter = 1#according to the dimension of the map
                for e in DemoMap['map']:
                    Root.update()
                    Cell[e] = dict(x=wCounter, y=hCounter, gfc=f'{e}')#cells are given an x,y and graphic
                    CellList.append(Cell[e])
                    SceneW.insert('insert', Cell[e]['gfc'])
                    wCounter += 1
                    if wCounter > DemoMap['w']:
                        Root.update()
                        wCounter = 1
                        hCounter += 1
                        SceneW.insert('insert', '\n')

            def refresh_map():#every time the user inputs a move, the map is refreshed
                Root.update()
                SceneW.delete(1.0, 'end')
                wCounter = 1
                for cell in CellList:
                    Root.update()
                    if cell['x'] == Player['x'] and cell['y'] == Player['y']:#this condition assigns a graphic to the temporary
                        tempGfc = Player['gfc']                              #variable which tells the function what graphic to print
                    else:
                        tempGfc = cell['gfc']
                    SceneW.insert('insert', tempGfc)
                    wCounter += 1
                    if wCounter > DemoMap['w']:
                        Root.update()
                        wCounter = 1
                        SceneW.insert('insert', '\n')
                move_player()
                
            def move_player():
                while True:
                    Root.update()
                    playerDirection = input("Which way? ")#input is used and takes w,s,a, or d to move in 4 directions.
                    if playerDirection == 'a':
                        if Player['x'] == 1:#if the user is at the edge of the map, it doesns't move the player coordinate.
                            EventW.insert('insert', 'Out of bounds.\n')
                            continue
                        Player['x'] -= 1
                    
                    elif playerDirection == 'd':
                        if Player['x'] == DemoMap['w']:
                            EventW.insert('insert', 'Out of bounds.\n')
                            continue
                        Player['x'] += 1
                    
                    elif playerDirection == 'w':
                        if Player['y'] == 1:
                            EventW.insert('insert', 'Out of bounds.\n')
                            continue
                        Player['y'] -= 1
                    
                    elif playerDirection == 's':
                        if Player['y'] == DemoMap['h']:
                            EventW.insert('insert', 'Out of bounds.\n')
                            continue
                        Player['y'] += 1
                    refresh_map()

            def spawn_player():#this is used for when the user loads a new map
                while True:
                    spawnBoolean = input("Spawn player?")
                    if spawnBoolean == 'y':
                        Player['x'] = 20
                        Player['y'] = 4
                        refresh_map()
                        break
                    else:
                        continue
                        
            initialize_map()
            spawn_player()
            move_player()

main()

