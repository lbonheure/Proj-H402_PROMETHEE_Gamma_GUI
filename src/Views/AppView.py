from customtkinter import (CTk, CTkTabview)
from Resources.Menu import Menu

class AppView(CTk):
    """
    A class to handle the view of the PROMETHEE Gamma GUI application

    Attributes
    ----------
    tabView : CTkTabView
        a tabView that will contain the 3 main tabs of the application
    dataTab : CTkFrame
        the data tab, first tab of the application
    resultTab : CTkFrame
        the result tab, second tab of the application
    helpForParametersTab : CTkFrame
        the help For Parameters tab, third tab of the application

    Methods
    -------
    show()
        show the app
    getTabs()
        return the 3 tabs of the app
    """

    class ViewListener:
        def menuChoice(self, choice:str):
            pass


    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.geometry("500x500")
        self.configure(cursor="arrow")
        self.minsize(500, 500)
        self.resizable(True, True)
        self.title("Promethee Gamma")

        self.menu = Menu(master=self, text="Menu", command=self.menuChoice, values=["new project", "save project", "load project", "quit"])

        self.tabview = CTkTabview(self, fg_color="#ffffff")
        self.dataTab = self.tabview.add("Data")
        self.dataTab.configure(border_color="#000080", corner_radius=5, fg_color="#ffffff")

        self.resultTab = self.tabview.add("Results")
        self.resultTab.configure(border_color="#000080", corner_radius=5, fg_color="#ffffff")

        self.helpForParametersTab = self.tabview.add("Help for Parameters")
        self.resultTab.configure(border_color="#000080", corner_radius=5, fg_color="#ffffff")

        self.listener = None


    def setListener(self, l:ViewListener):
        self.listener = l


    def show(self):
        """Show the app
        """
        self.menu.pack(anchor="nw", side="top", pady=0, ipady=0)
        self.tabview.pack(expand=True, fill="both", pady=0, ipady=0)
        

    def getTabs(self):
        """Return the 3 tabs of the app

        Return
        ------
        (dataTab, resultTab, helpForParametersTab) : Tuple(CTkFrame, CTkFRame, CTkFrame)
            the 3 tabs of the app
        """
        return (self.dataTab, self.resultTab, self.helpForParametersTab)
    

    def setTab(self, name:str):
        self.tabview.set(name)


    def menuChoice(self, choice:str):
        self.listener.menuChoice(choice)


