from abc import ABC, abstractmethod

class IFileSystemItem(ABC): # Interfaz del patron
    @abstractmethod
    def display(self, ident = " "):
        pass

class AppFile(IFileSystemItem): # objeto para archivos que tiene nombre he implementa display
    def __init__(self, name) -> None:
        self._name = name 
    def display(self, ident="   "):
        print(f"{ident} - {self.__class__.__name__} : {self._name}")

class Folder(IFileSystemItem): # objeto para folers define su display y add item 
    def __init__(self, name) -> None:
        self._name = name 
        self._items = []
    def add_item(self, item):
        self._items.append(item)
    def display(self, ident=""):
        print(f"|{ident} - {self.__class__.__name__} : {self._name}")
        for item in self._items:
            item.display( ident + "     " )

file1 = AppFile("File1")
file2 = AppFile("File2")
file3 = AppFile("File3")

folder1 = Folder("Folder1")
folder2 = Folder("Folder2")

folder1.add_item(file1)
folder1.add_item(file2)
folder2.add_item(file3)

root = Folder("root")
root.add_item(folder1)
root.add_item(folder2)

root.display()