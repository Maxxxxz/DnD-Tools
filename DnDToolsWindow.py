#   Michael Cooper

import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
import sys

import pages

#   Create each module its own screen class; use place() and lift() methods to display

#   Create pop out "monster manual" window for easy viewing of monster stats.
#   Basically just big table able to search through it

class Application(tk.Frame):

    selectedFiles = []  #empty list of files

    def __init__(self, master=None):
        master.title("Template")                                    #change title here
        master.geometry("600x600")                                  #change window size here
        master.resizable(width=False, height=False)                 #resizable?
        tk.Frame.__init__(self, master, relief=tk.GROOVE)
        self.menubar = tk.Menu(self)

        self.contentFrame = tk.Frame(master, width=100, height=100)
        self.contentFrame.pack(anchor=tk.NW, fill=tk.BOTH, expand=True)

        self.pages = []

        self.addContent(self.contentFrame)

        self.menus = []

        self.addMenus(self.menus)

        for page in self.pages:     # place all pages
            page.place(in_=self.contentFrame, x=0, y=0, relwidth=1, relheight=1)

        self.pages[0].show()        # begin at main page

        master.config(menu=self.menubar)

        # Binding Control + number to show different pages



        self.bind_all("<Control-Key-0>", self.pages[0].show)    # main menu
        self.bind_all("<Control-Key-1>", self.pages[1].show)    # RNG
        self.bind_all("<Control-Key-2>", self.pages[2].show)    # Name Gen
        self.bind_all("<Control-Key-3>", self.pages[3].show)    # Character Gen
        self.bind_all("<Control-Key-4>", self.pages[4].show)    # NPC Gen
        self.bind_all("<Control-Key-5>", self.pages[5].show)    # Story Gen
        self.bind_all("<Control-Key-6>", self.pages[6].show)    # Settlement Gen
        self.bind_all("<Control-Key-7>", self.pages[7].show)    # Encounter Gen

    def addMenus(self, menus=None):

        menus.append(tk.Menu(self.menubar, tearoff=0))  # create dropdown menu File

        self.menubar.add_cascade(label="File", underline=0, menu=menus[0])
        menus[0].add_command(label="Open", command=self.openFiles)
        menus[0].add_command(label="DEBUG|Print Open Files", command=lambda: print(self.selectedFiles))
        menus[0].add_command(label="Clear Selections", command=self.clearSelections)
        menus[0].add_separator()
        menus[0].add_command(label="Exit", command=self.master.quit)

        menus.append(tk.Menu(self.menubar, tearoff=0))  # create dropdown menu View

        self.menubar.add_cascade(label="Generators", underline=0, menu=menus[1])
        menus[1].add_command(label="Main Menu", command=self.pages[0].lift, accelerator="Control+0")
        menus[1].add_command(label="Random Number Generator", command=self.pages[1].lift, accelerator="Control+1")
        menus[1].add_command(label="Name Generator", command=self.pages[2].lift, accelerator="Control+2")
        menus[1].add_command(label="Character Generator", command=self.pages[3].lift, accelerator="Control+3")
        menus[1].add_command(label="NPC Generator", command=self.pages[4].lift, accelerator="Control+4")
        menus[1].add_command(label="Story Generator", command=self.pages[5].lift, accelerator="Control+5")
        menus[1].add_command(label="Settlement Generator", command=self.pages[6].lift, accelerator="Control+6")
        menus[1].add_command(label="Encounter Generator", command=self.pages[7].lift, accelerator="Control+7")

    def clearSelections(self):
        self.selectedFiles.clear()

    def addContent(self, contentFrame=None):                        #add content to contentFrame here
        self.pages.append(pages.Menu())
        self.pages.append(pages.RollTheDice())
        self.pages.append(pages.NameGen())
        self.pages.append(pages.CharacterGen())
        self.pages.append(pages.NPCGen())
        self.pages.append(pages.StoryGen())
        self.pages.append(pages.SettlementGen())
        self.pages.append(pages.EncounterGen())

        # rest of pages places below

        # pages placed here
        # self.lb = tk.Listbox(contentFrame, width=30)
        # self.lb.pack(anchor=tk.CENTER)

    def openFiles(self):                                            #change filedialog config as needed
        self.selectedFiles += filedialog.askopenfilenames(initialdir="Documents", title="Select Files", filetypes=[("Json Files","*.json")])
        # #updating list inside contentFrame
        # list = self.contentFrame.winfo_children()
        # if isinstance(list[0], tk.Listbox):
        #     list[0].insert(tk.END, self.selectedFiles)

root = tk.Tk()
application = Application(root)
application.pack()
root.mainloop()