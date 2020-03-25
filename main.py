import src.hmi.Window as win
import src.logic.AppManager as appManager

def main():
    manager = appManager.AppManager()
    window = win.Window(manager)
    window.geometry("200x300")
    window.title("Recherche Opérationnelle")
    manager.setWindow(window)
    window.mainloop()
    





if __name__ == "__main__":
    main()