from customtkinter import (CTkEntry, DoubleVar)

from ...Models.DataTabModels.Alternative import Alternative


class UnitRow:
    """
    A class to display the row of a unit (an alternative)

    Attributes
    ----------
    master : CTkFrame
        the master frame
    row : int
        the row for grid coordinate of the UnitRow
    col : int
        the column for grid coordinate of the UnitRow
    alternative : Alternative
        the alternative of which it is the row
    nameEntry : CTkEntry
        the entry to modify the altenative name
    valuesEntries : list[CTkEntry]
        a list that will contain all entries to modify evaluations of the altenative
    """

    def __init__(self, master, row:int, col:int, alternative:Alternative) -> None:
        """
        Parameters
        ----------
        master : CTkFrame
            the master frame
        row : int
            the row for grid coordinate of the UnitRow
        col : int
            the column for grid coordinate of the UnitRow
        alternative : Alternative
            the alternative of which it is the row
        """
        self.master=master
        self.row = row
        self.col = col
        self.alternative = alternative
        self.nameEntry = CTkEntry(master=self.master, textvariable=alternative.getName(), width=180)
        self.valueEntries = []
        for i in range(alternative.getSize()):
            self.valueEntries.append(CTkEntry(master=self.master, textvariable=alternative.getEvaluation(i), width=120))

    
    def show(self):
        """Show the row
        """
        self.nameEntry.grid(row=self.row, column=self.col, sticky="e")
        for i in range(self.alternative.getSize()):
            self.col += 1
            self.valueEntries[i].grid(row=self.row, column=self.col)

    
    def add_column(self, value:DoubleVar):
        """Add a column to the row

        Parameters
        ----------
        value : DoubleVar
            The value to add in the last column
        """
        self.valueEntries.append(CTkEntry(master=self.master, textvariable=value, width=120))
        self.col += 1
        self.valueEntries[-1].grid(row=self.row, column=self.col)


    def destroy(self) -> None:
        """Destroy the row
        """
        self.nameEntry.destroy()
        for i in self.valueEntries:
            i.destroy()


    def del_column(self) -> None:
        """Destroy the last column of the row
        """
        self.valueEntries[-1].destroy()
        self.valueEntries.pop()
        self.col -= 1