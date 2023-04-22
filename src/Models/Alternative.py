from customtkinter import (StringVar, DoubleVar)

class Alternative:
    def __init__(self, name:DoubleVar=None, evaluations:list[DoubleVar]=[]) -> None:
        self.name = name
        self.evaluations = evaluations


    def setName(self, name:StringVar) -> None:
        self.name = name


    def addEvaluations(self, evaluation:DoubleVar) -> None:
        self.evaluations.append(evaluation)


    def deleteEvaluation(self, index:int=-1) -> None:
        self.evaluations.pop(index)

    
    def getName(self) -> StringVar:
        return self.name
    

    def getName_str(self) -> str:
        return self.name.get()
    

    def getEvaluation(self, index=-1) -> DoubleVar:
        return self.evaluations[index]
    

    def getSize(self) -> int:
        return len(self.evaluations)