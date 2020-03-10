import src.hmi.Window as win
import src.logic.AppManager as appManager

def main():
    window = win.Window()
    manager = appManager.AppManager()
    window.setManager(manager)
    manager.setWindow(window)
    window.mainloop()
    





if __name__ == "__main__":
    main()