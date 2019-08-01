#   Michael Cooper

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import *
import sys
import webbrowser
import requests
import json

import pages

#   Create each module its own screen class; use place() and lift() methods to display

#   Create pop out "monster manual" window for easy viewing of monster stats.
#   Basically just big table able to search through it

class Application(tk.Frame):

    selectedFiles = []  #empty list of files

    def __init__(self, master=None):
        master.title("Dungeons And Dragons Tools")                                    #change title here
        master.geometry("800x800")                                  #change window size here
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

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Binding Control + number to show different pages

        self.bind_all("<Control-Key-0>", self.pages[0].show)    # main menu
        self.bind_all("<Control-Key-1>", self.pages[1].show)    # RNG
        self.bind_all("<Control-Key-2>", self.pages[2].show)    # Name Gen
        self.bind_all("<Control-Key-3>", self.pages[3].show)    # Character Gen
        self.bind_all("<Control-Key-4>", self.pages[4].show)    # NPC Gen
        self.bind_all("<Control-Key-5>", self.pages[5].show)    # Story Gen
        self.bind_all("<Control-Key-6>", self.pages[6].show)    # Settlement Gen
        self.bind_all("<Control-Key-7>", self.pages[7].show)    # Encounter Gen

        self.versioninfo = self.getVersionInfo()

        # print("Version: " + self.versioninfo["version"])
        # changestr = "Changes: "
        #
        # for note in self.versioninfo["changes"]:
        #     changestr += note + " "
        # print(changestr)

        #self.recentversion = requests.get()

    def getVersionInfo(self):
        with open(".//json//version.json") as j:
            return json.load(j)

    def addMenus(self, menus=None):

        menus.append(tk.Menu(self.menubar, tearoff=0))  # create dropdown menu File

        self.menubar.add_cascade(label="File", underline=0, menu=menus[0])
        menus[0].add_command(label="Open Character", command=self.openFiles)
        menus[0].add_command(label="Open NPC", command=self.openFiles)
        menus[0].add_command(label="Open Map", command=self.openFiles)
        menus[0].add_command(label="Open Encounter", command=self.openFiles)
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

        menus.append(tk.Menu(self.menubar, tearoff=0))  # create dropdown menu Help
        self.menubar.add_cascade(label="Help", underline=0, menu=menus[2])
        menus[2].add_command(label="Github Page", command=lambda: self.githubButton())
        menus[2].add_command(label="Github Page", command=lambda: self.helpButton())
        menus[2].add_command(label="Support Me :)", command=lambda: self.supportmeButton())
        menus[2].add_command(label="About", command=lambda: self.aboutButton())

    def clearSelections(self):
        self.selectedFiles.clear()

    def supportmeButton(self):
        webbrowser.open("https://github.com/Maxxxxz/DnD-Tools")

    def helpButton(self):
        webbrowser.open("https://github.com/Maxxxxz/DnD-Tools")

    def aboutButton(self):
        vinfo = "Newest Version: " + "\n"# + self.recentversion["version"]
        vinfo += "Current Version: " + self.versioninfo["version"] + "\n"
        ch = '\n'.join(self.versioninfo["changes"])
        vinfo += ch
        messagebox.showinfo("About", vinfo)
        pass
        # get current version from local json file; read most up to date version from github; display latest changes

    def githubButton(self):
        webbrowser.open("https://github.com/Maxxxxz/DnD-Tools")

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

    # add multiple open files to capture all file uses ex: openCharacter, openMap, openEncounter, etc...
    def openFiles(self):                                            #change filedialog config as needed
        self.selectedFiles += filedialog.askopenfilenames(initialdir="Documents", title="Select Files", filetypes=[("Json Files","*.json")])

root = tk.Tk()
application = Application(root)
application.pack()
root.mainloop()
