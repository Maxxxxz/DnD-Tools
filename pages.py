#   Michael Cooper

import tkinter as tk
from random import randrange

class Page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    def show(self, event=None):
        self.lift()

#   Main menu; navigate to any gens (have gens in top menu bar as well)
class Menu(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(self, text="Main Menu")
        label.pack(side="top", fill="both", expand=True)

#   standard rolls + # of dice per each
#   D4, D6, D8, D10, D12, D20
class RollTheDice(Page):
    def __init__(self):
        Page.__init__(self)
        #self.master.title("Dungeons and Dragons Tools - Random Number Generator")
        label = tk.Label(self, text="Random Number Generator")
        #label.grid(column=0, row=0, padx=(0, 0), pady=(20, 40))
        label.place(x=400, y=25, anchor="center")       # Place label at top of screen, then use grid for rest



        ########################################################
        #   pady=100 to keep row a good distance from the top
        D4Num = tk.Spinbox(self, from_=1, to_=100, width=5)
        D4Num.grid(column=0, row=1, padx=(230, 0), pady=(100, 0))
        D4 = tk.Button(self, text="xD4", command=lambda: D4Out.config(text=1+randrange(0, int(D4Num.get())*4)))
        D4.grid(column=1, row=1, padx=(10, 0), pady=(100, 0))
        D4Out = tk.Label(self, text="", width=5)
        D4Out.grid(column=2, row=1, padx=(10, 0), pady=(100, 0))
        ########################################################

        ########################################################
        #   pady=10 because already a good distance from top
        D6Num = tk.Spinbox(self, from_=1, to_=100, width=5)
        D6Num.grid(column=0, row=2, padx=(230, 0), pady=(10, 0))
        D6 = tk.Button(self, text="xD6", command=lambda: D6Out.config(text=1+randrange(0, int(D6Num.get())*6)))
        D6.grid(column=1, row=2, padx=(10, 0), pady=(10, 0))
        D6Out = tk.Label(self, text="", width=5)
        D6Out.grid(column=2, row=2, padx=(10, 0), pady=(10, 0))
        ########################################################

        ########################################################
        D8Num = tk.Spinbox(self, from_=1, to_=100, width=5)
        D8Num.grid(column=0, row=3, padx=(230, 0), pady=(10, 0))
        D8 = tk.Button(self, text="xD8", command=lambda: D8Out.config(text=1+randrange(0, int(D8Num.get())*8)))
        D8.grid(column=1, row=3, padx=(10, 0), pady=(10, 0))
        D8Out = tk.Label(self, text="", width=5)
        D8Out.grid(column=2, row=3, padx=(10, 0), pady=(10, 0))
        ########################################################

        ########################################################
        DCRNum = tk.Spinbox(self, from_=1, to_=10000, width=5)
        DCRNum.grid(column=0, row=4, padx=(230, 0), pady=(10, 0))
        DCR = tk.Button(self, text="D#", command=lambda: DCROut.config(text=1+randrange(0, int(DCRNum.get()))))
        DCR.grid(column=1, row=4, padx=(10, 0), pady=(10, 0))
        DCROut = tk.Label(self, text="", width=5)
        DCROut.grid(column=2, row=4, padx=(10, 0), pady=(10, 0))
        ########################################################

        ########################################################
        D10Num = tk.Spinbox(self, from_=1, to_=100, width=5)
        D10Num.grid(column=4, row=1, padx=(100, 0), pady=(100, 0))
        D10 = tk.Button(self, text="xD10", command=lambda: D10Out.config(text=1+randrange(0, int(D10Num.get())*10)))
        D10.grid(column=5, row=1, padx=(10, 0), pady=(100, 0))
        D10Out = tk.Label(self, text="", width=5)
        D10Out.grid(column=6, row=1, padx=(10, 0), pady=(100, 0))
        ########################################################

        ########################################################
        D12Num = tk.Spinbox(self, from_=1, to_=100, width=5)
        D12Num.grid(column=4, row=2, padx=(100, 0), pady=(10, 0))
        D12 = tk.Button(self, text="xD12", command=lambda: D12Out.config(text=1+randrange(0, int(D12Num.get())*12)))
        D12.grid(column=5, row=2, padx=(10, 0), pady=(10, 0))
        D12Out = tk.Label(self, text="", width=5)
        D12Out.grid(column=6, row=2, padx=(10, 0), pady=(10, 0))
        ########################################################

        ########################################################
        D20Num = tk.Spinbox(self, from_=1, to_=100, width=5)
        D20Num.grid(column=4, row=3, padx=(100, 0), pady=(10, 0))
        D20 = tk.Button(self, text="xD20", command=lambda: D20Out.config(text=1+randrange(0, int(D20Num.get())*20)))
        D20.grid(column=5, row=3, padx=(10, 0), pady=(10, 0))
        D20Out = tk.Label(self, text="", width=5)
        D20Out.grid(column=6, row=3, padx=(10, 0), pady=(10, 0))
        ########################################################

        ########################################################
        D100Num = tk.Spinbox(self, from_=1, to_=100, width=5)
        D100Num.grid(column=4, row=4, padx=(100, 0), pady=(10, 0))
        D100 = tk.Button(self, text="xD100", command=lambda: D100Out.config(text=1+randrange(0, int(D100Num.get())*100)))
        D100.grid(column=5, row=4, padx=(10, 0), pady=(10, 0))
        D100Out = tk.Label(self, text="", width=5)
        D100Out.grid(column=6, row=4, padx=(10, 0), pady=(10, 0))
        ########################################################

#   Different races/genders + territory names
class NameGen(Page):
    def __init__(self):
        Page.__init__(self)
        #self.master.wm_title("Dungeons and Dragons Tools - Name Generator")
        label = tk.Label(self, text="Name Generator")
        label.pack(side="top", fill="both", expand=True)

#   lock options on some info boxes
class CharacterGen(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(self, text="Character Generator")
        label.pack(side="top", fill="both", expand=True)

#   lock options on some info boxes
class NPCGen(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(self, text="NPC Generator")
        label.pack(side="top", fill="both", expand=True)

#   character/campaign story gen options
class StoryGen(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(self, text="Story Generator")
        label.pack(side="top", fill="both", expand=True)

#   size/vendor options; would LOVE to create images for them perhaps using PIL?
class SettlementGen(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(self, text="Settlement Generator")
        label.pack(side="top", fill="both", expand=True)

#   base on number of players and the average level of each.
#   make note of custom encounters based on environment will be much better
class EncounterGen(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(self, text="Encounter Generator")
        label.pack(side="top", fill="both", expand=True)