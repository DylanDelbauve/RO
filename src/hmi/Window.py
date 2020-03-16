from tkinter import *
from tkinter import filedialog as fd

class Window(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.createMenu()
        self.__listCities = Listbox()
        self.__listCities.pack()
        self.manager = None

    def openfile(self):
        file = open(fd.askopenfilename(), "r")
        cities = self.manager.readFile(file)
        self.showCities(cities)
        

    def createMenu(self):
        menu = Menu(self)
        menuFile = Menu(menu, tearoff=0)
        menuFile.add_command(label="Import", command=self.openfile)
        menu.add_cascade(label="File", menu=menuFile)
        self.config(menu = menu)

    def setManager(self, manager):
        self.manager = manager

    def showCities(self,cities):
        for city in cities:
            self.__listCities.insert('end', city.__str__())
            
