from customtkinter import (CTkLabel, CTkButton)

from .QuestionsTabView import QuestionsTabView


class PreferenceLearningView(QuestionsTabView.Listener):
    """
    A class to display questions and others component for prefenrence learning algorithm

    Attributes
    ----------
    master : CTkFrame
        the parent master frame
    questionsTabView : CTkTabView
        the tabView that will contain the questions
    explanationLabel : CTkLabel
        a label to display the explanation text for preference learning algorithm
    generateButton : CTkButton
        a button to generate questions for preference learning algorithm
    confirmButton : CTkButton
        a button to confirm the answers
    nextButton : CTkButton
        a button to generate the next question
    Ilabel : CTkLabel
        a label to display the value of the indifference parameter
    Jlabel : CTkLabel
        a label to display the value of the incomparability parameter
    Plabel : CTkLabel
        a label to display the value of the preference parameter
    applyButton : CTkButton
        a button to apply the results in result tab
    cancelButton : CTkButton
        a button to cancel confirmation of answers
    quitButton : CTkButton
        a button to quit preference learning view
    row : int
        the row for positionning elements with grid method
    listener : ViewListener
        the listener of this view
    """

    class ViewListener:
        """
        An interface for the listener of this view
        """

        def generate(self):
            """Generate questions
            """
            pass

        def confirm(self):
            """Control the reaction of the app after a click on the confirm button
            """
            pass

        def apply(self):
            """Control the reaction of the app after a click on the apply button
            """
            pass

        def next(self):
            """Control the reaction of the app after a click on the next button
            """
            pass

        def updateInmcq(self):
            """Handle an update in mcq
            """
            pass

        def cancel(self):
            """Control the reaction of the app after a click on the cancel button
            """
            pass

        def quit(self):
            """Control the reaction of the app after a click on the quit button
            """
            pass


    def __init__(self, master) -> None:
        """
        Parameters
        ----------
        master : CTkFrame
            the master frame
        """
        self.master = master
        self.questionsTabView = None
        explanation = "In order to help determine the 3 parameters introduced by the PROMETHEE Gamma method, it is necessary to know your opinion on a small number of pairwise comparisons between alternatives. Please answer the questions below."
        self.explanationLabel = CTkLabel(master=self.master, text=explanation, text_color="#000000", wraplength=580)
        self.generateButton = CTkButton(master=self.master, text="Generate questions", fg_color="#6cffff", text_color="#000000", corner_radius=5, command=self.generate)
        self.confirmButton = CTkButton(master=self.master, text="Confirm", fg_color="#6cffff", text_color="#000000", corner_radius=5, command=self.confirm)
        self.nextButton = CTkButton(master=self.master, text="Next", fg_color="#6cffff", text_color="#000000", corner_radius=5, command=self.next)
        self.Ilabel = CTkLabel(master=self.master, text="Ti = 0 - 1", text_color="#000000")
        self.Jlabel = CTkLabel(master=self.master, text="Tj = 0 - 1", text_color="#000000")
        self.Plabel = CTkLabel(master=self.master, text="Pf = 1 - infinity", text_color="#000000")
        self.applyButton = CTkButton(master=self.master, text="Use results in results tab", fg_color="#6cffff", text_color="#000000", corner_radius=5, command=self.apply)
        self.cancelButton = CTkButton(master=self.master, text="Cancel", fg_color="#6cffff", text_color="#000000", corner_radius=5, command=self.cancel)
        self.quitButton = CTkButton(master=self.master, text="Quit", fg_color="#6cffff", text_color="#000000", corner_radius=5, command=self.quit)
        self.row = 0
        self.listener = None


    def setListener(self, l:ViewListener):
        """Set the listener

        Parameters
        ----------
        l : ViewListener
            the new listener
        """
        self.listener = l


    def show(self):
        """Show the preference learning components
        """
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.explanationLabel.grid(row=self.row, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="n")
        self.row +=1
        self.generateButton.grid(row=self.row, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="n")
        self.row +=1
        self.Ilabel.grid(row=self.row, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="n")
        self.row +=1
        self.Jlabel.grid(row=self.row, column=0, columnspan=2, padx=10, pady=(1, 0), sticky="n")
        self.row +=1
        self.Plabel.grid(row=self.row, column=0, columnspan=2, padx=10, pady=(1, 0), sticky="n")
        self.row +=1
        self.quitButton.grid(row=self.row, column=0, columnspan=2, padx=10, pady=(10,0), sticky="n")

    
    def showNextQuestion(self, question:tuple, criteriaNames:list) -> None:
        """Show the next question of preference learning algorithm

        Parameters
        ----------
        question : Tuple(Alternative, Alternative, IntVar)
            the "question", i.e. the two alternatives that will be compared and the value of preference (in the IntVar): 
            0 for indifference ; 1 for preference ; -1 for incomparability
        """
        self.questionsTabView.addQuestion(question, criteriaNames)


    def next(self):
        """Handle click on nextButton
        """
        self.listener.next()


    def confirm(self):
        """Handle click on confirmButton
        """
        self.listener.confirm()


    def apply(self):
        """Handle click on applyButton
        """
        self.listener.apply()


    def resetResults(self):
        """Reset the results (reset labels)
        """
        self.Ilabel.configure(text="Ti = 0 - 1")
        self.Jlabel.configure(text="Tj = 0 - 1")
        self.Plabel.configure(text="Pf = 1 - infinity")
        self.Ilabel.update()
        self.Jlabel.update()
        self.Plabel.update()
        

    def generate(self):
        """Reset algorithm and (re)start it
        """
        self.listener.generate()


    def createQuestionsTab(self):
        """Create the questions tab
        """
        if self.questionsTabView != None:
            infos = self.questionsTabView.grid_info()
            row = infos["row"]
            self.questionsTabView.destroy()
        else:
            row = self.row
            self.row += 2
        self.questionsTabView = QuestionsTabView(master=self.master, fg_color="#ffffff")
        self.questionsTabView.setListener(self)
        self.questionsTabView.grid(row=row, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="n")


    def showResults(self, results:tuple):
        """Show the results in labels (ILabel, JLabel and PLabel)

        Parameters
        ----------
        results : tuple[DoubleVar, DoubleVar, DoubleVar, DoubleVar, DoubleVar, DoubleVar]
            results = (Imin, Imax, Jmin, Jmax, Pmin, Pmax) ; these are the resulting values of preference learning algorithm
        """
        (Imin, Imax, Jmin, Jmax, Pmin, Pmax) = results
        Imin = round(Imin,2)
        Imax = round(Imax,2)
        Jmin = round(Jmin,2)
        Jmax = round(Jmax,2)
        Pmin = round(Pmin,2)
        Pmax = round(Pmax,2)
        if Imin == Imax:
            Itext = "Ti = " + str(Imin)
        else:
            Itext = "Ti = " + str(Imin) + " - " + str(Imax)
        if Jmin == Jmax:
            Jtext = "Tj = " + str(Jmin)
        else:
            Jtext = "Tj = " + str(Jmin) + " - " + str(Jmax)
        if Pmin == Pmax:
            if Pmin > 100:
                Ptext = "Pf = infinity"
            else:
                Ptext = "Pf = " + str(Pmin)
        else:
            Ptext = "Pf = " + str(Pmin) + " - "
            if Pmax > 100.0:
                Ptext += "infinity"
            else:
                Ptext += str(Pmax)
        self.Ilabel.configure(text=Itext)
        self.Jlabel.configure(text=Jtext)
        self.Plabel.configure(text=Ptext)
        self.Ilabel.update()
        self.Jlabel.update()
        self.Plabel.update()


    def updateInmcq(self):
        """Handle event in questions
        """
        self.listener.updateInmcq()


    def showNextConfirm(self, end:bool):
        """Hide apply and cancel button and show next and confirm button
        """
        self.applyButton.grid_forget()
        self.cancelButton.grid_forget()
        self.row -= 1
        if end:
            self.nextButton.grid_forget()
            self.confirmButton.grid(row=self.row, column=0, columnspan=2, padx=10, pady=(15, 0), sticky="n")
        else:
            self.nextButton.grid(row=self.row, column=0, padx=10, pady=(15, 0), sticky="e")
            self.confirmButton.grid(row=self.row, column=1, padx=10, pady=(15, 0), sticky="w")
        self.row += 1
        self.quitButton.grid_configure(row=self.row)


    def showApplyCancel(self):
        """Hide next and confirm button and show apply and cancel button
        """
        self.nextButton.grid_forget()
        self.confirmButton.grid_forget()
        self.row -= 1
        self.applyButton.grid(row=self.row, column=0, padx=10, pady=(15, 0), sticky="e")
        self.cancelButton.grid(row=self.row, column=1, padx=10, pady=(15, 0), sticky="w")
        self.row += 1
        self.quitButton.grid_configure(row=self.row)


    def cancel(self):
        """Handle click on cancelButton
        """
        self.listener.cancel()


    def quit(self):
        """Handle click on quitButton
        """
        self.listener.quit()


    def resetView(self):
        """Reset the view, i.e. destroy all widget displayed
        """
        for w in self.master.winfo_children():
            w.destroy()
        self.master.grid_columnconfigure(1, weight=0)