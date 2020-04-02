from tkinter import *
from tkinter import filedialog as fd


class Window(Tk):

    def __init__(self, manager):
        Tk.__init__(self)
        self.manager = manager
        self.create_menu()
        self.cost = Label(text="")
        self.cost.pack()
        self.listCities = Listbox()
        self.listCities.pack()
        self.result = Label(text="")
        self.result.pack()

    def open_file(self):
        file = open(fd.askopenfilename(), "r")
        cities = self.manager.read_file(file)
        self.show_cities(cities)
        file.close()

    def export_file(self):
        file = open(fd.asksaveasfilename(title="Unamed", filetypes=(('text files', 'txt'),)), "w")
        file.write(self.result['text'])
        file.close()

    def create_menu(self):
        menu = Menu(self)
        menu_file = Menu(menu, tearoff=0)
        menu_file.add_command(label="Import", command=self.open_file)
        menu_file.add_command(label="Export", command=self.export_file)
        menu.add_cascade(label="File", menu=menu_file)
        menu_algo = Menu(menu, tearoff=0)
        menu.add_cascade(label="Algo", menu=menu_algo)
        menu_algo.add_command(label="Random", command=self.random_algo)
        menu_algo.add_command(label="Increasing", command=self.increase_algo)
        menu_algo.add_command(label="Neighbour", command=self.search_near)
        menu_algo.add_command(label="Local", command=self.search_local)
        menu.add_command(label="Cost", command=self.cost)

        self.config(menu=menu)

    def set_manager(self, manager):
        self.manager = manager

    def show_cities(self, cities):
        for city in cities:
            self.listCities.insert('end', city.str())

    def random_algo(self):
        self.manager.result(0)
        self.result['text'] = self.manager.__str__()

    def increase_algo(self):
        self.manager.result(1)
        self.result['text'] = self.manager.__str__()

    def search_near(self):
        self.manager.result(2)
        self.result['text'] = self.manager.__str__()

    def search_local(self):
        self.manager.result(3)
        self.result['text'] = self.manager.__str__()

    def cost(self):
        self.cost['text'] = self.manager.cost()
