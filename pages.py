#   Michael Cooper

import tkinter as tk

class Page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    def show(self):
        self.lift()

#   Main menu; navigate to any gens (have gens in top menu bar as well)
class Menu(Page):
    def __init__(self):
        Page.__init__(self)

#   standard dice rolls + custom roll
class RollTheDice(Page):
    def __init__(self):
        Page.__init__(self)

#   Different races/genders + territory names
class NameGen(Page):
    def __init__(self):
        Page.__init__(self)

#   lock options on some info boxes
class CharacterGen(Page):
    def __init__(self):
        Page.__init__(self)

#   lock options on some info boxes
class NPCGen(Page):
    def __init__(self):
        Page.__init__(self)

#   character/campaign story gen options
class StoryGen(Page):
    def __init__(self):
        Page.__init__(self)

#   size/vendor options; would LOVE to create images for them perhaps using PIL?
class SettlementGen(Page):
    def __init__(self):
        Page.__init__(self)

#   base on number of players and the average level of each.
#   make note of custom encounters based on environment will be much better
class EncounterGen(Page):
    def __init__(self):
        Page.__init__(self)