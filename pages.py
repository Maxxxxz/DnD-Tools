#   Michael Cooper

import tkinter as tk

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

#   standard dice rolls + custom roll
class RollTheDice(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(self, text="Random Number Generator")
        label.grid(column=1, row=0, padx=(10, 0), pady=(10, 0))
        label2 = tk.Label(self, text="test")
        label2.grid(column=2, row=0, padx=(0, 0), pady=(0, 0))
        label3 = tk.Label(self, text="test3")
        label3.grid(column=2, row=1, padx=(0, 0), pady=(0, 0))

#   Different races/genders + territory names
class NameGen(Page):
    def __init__(self):
        Page.__init__(self)
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