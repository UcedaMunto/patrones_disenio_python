from abc import ABC, abstractmethod

class IFileSystemItem(ABC): # Interfaz del patron
    @abstractmethod
    def display(self, ident = " "): #obliga a definir un metodo dispĺay comun para las clases
        pass

class AppFile(IFileSystemItem): # el objeto archivo imlementa y por tanto define a display para su caso concreto
    def __init__(self, name) -> None: # define un parametro para la construccion de este objeto
        self._name = name 
    def display(self, ident="   "):
        print(f"{ident} - {self.__class__.__name__} : {self._name}")

class Folder(IFileSystemItem): # objeto implementa y por tanto define display y ademas mantiene un array de objetos
    def __init__(self, name) -> None:
        self._name = name 
        self._items = []
    def add_item(self, item):
        self._items.append(item)
    def display(self, ident=""):
        print(f"|{ident} - {self.__class__.__name__} : {self._name}")
        for item in self._items:  # recorrer y mostrar 
            item.display( ident + "     " )

file1 = AppFile("File1") # construye y agrega el nombre a los archivos
file2 = AppFile("File2")
file3 = AppFile("File3")

folder1 = Folder("Folder1") #construye los folders
folder2 = Folder("Folder2")

folder1.add_item(file1) 
folder1.add_item(file2)
folder2.add_item(file3)

root = Folder("root")
root.add_item(folder1)
root.add_item(folder2)

root.display() # muestra los elementos