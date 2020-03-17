from tkinter import *
from functools import partial
from tkinter import filedialog as fd

class Window(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.createMenu()
        self.__listCities = Listbox()
        self.__listCities.pack()
        self.result = Label(text="")
        self.result.pack()
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
        menuAlgo = Menu(menu, tearoff=0)
        menu.add_cascade(label="Algo", menu=menuAlgo)
        menuAlgo.add_command(label="Random", command=partial(self.choiceAlgo,0))
        menuAlgo.add_command(label="Increasing", command=partial(self.choiceAlgo,1))
        menuAlgo.add_command(label="neighbour", command=partial(self.choiceAlgo,2))

        self.config(menu = menu)

    def setManager(self, manager):
        self.manager = manager

    def showCities(self,cities):
        for city in cities:
            self.__listCities.insert('end', city.__str__())
    
    def choiceAlgo(self,algo):
        if algo == 0:
            temp = self.manager.random()
        elif algo == 1:
            pass
        elif algo == 2:
            pass
        self.result['text'] = temp

            
