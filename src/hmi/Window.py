from tkinter import *
from functools import partial
from tkinter import filedialog as fd

class Window(Tk):

    def __init__(self,manager):
        Tk.__init__(self)
        self.manager = manager
        self.createMenu()
        self.cost = Label(text="")
        self.cost.pack()
        self.listCities = Listbox()
        self.listCities.pack()
        self.result = Label(text="")
        self.result.pack()
        
        

    def openFile(self):
        file = open(fd.askopenfilename(), "r")
        cities = self.manager.readFile(file)
        self.showCities(cities)
        file.close()
        
    def exportFile(self):
        file = open(fd.asksaveasfilename(title="Unamed", filetypes=(('text files', 'txt'),)), "w")
        file.write(self.result['text'])
        file.close()

    def createMenu(self):
        menu = Menu(self)
        menuFile = Menu(menu, tearoff=0)
        menuFile.add_command(label="Import", command=self.openFile)
        menuFile.add_command(label="Export", command=self.exportFile)
        menu.add_cascade(label="File", menu=menuFile)
        menuAlgo = Menu(menu, tearoff=0)
        menu.add_cascade(label="Algo", menu=menuAlgo)
        menuAlgo.add_command(label="Random", command=self.randomAlgo)
        menuAlgo.add_command(label="Increasing", command=self.increaseAlgo)
        menuAlgo.add_command(label="neighbour", command=self.searchNear)
        menu.add_command(label="Cost", command=self.cost)

        self.config(menu = menu)

    def setManager(self, manager):
        self.manager = manager

    def showCities(self,cities):
        for city in cities:
            self.listCities.insert('end', city.str())
    
    def randomAlgo(self):
        self.result['text'] = self.manager.random()

    def increaseAlgo(self):
        self.result['text'] = self.manager.increasing()

    def searchNear(self):
        self.result['text'] = self.manager.searchNear()

    def cost(self):
        self.cost['text'] = self.manager.cost()

            
