import tkinter as tk

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

Root.mainloop()
